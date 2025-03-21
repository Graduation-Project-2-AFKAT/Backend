from datetime import timedelta

from django.db.models import Q
from django.http import Http404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from afkat_auth.permissions import UserIsOwnerOrReadOnly
from afkat_home.api.filters import PostFilterSet
from afkat_home.api.serializers import (
    PostSerializer,
    TagSerializer,
    PostDetailSerializer,
)
from afkat_home.models import Tag, Post


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=["get"], detail=True, name="Posts with this Tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        page = self.paginate_queryset(tag.posts)

        if page is not None:
            post_serializer = PostSerializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(post_serializer.data)
        post_serializer = PostSerializer(
            tag.posts, many=True, context={"request": request}
        )
        return Response(post_serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [UserIsOwnerOrReadOnly | IsAdminUser]
    queryset = Post.objects.all()
    filterset_class = PostFilterSet
    ordering_fields = ["published_at", "author", "title", "slug"]

    def get_queryset(self):
        if self.request.user.is_anonymous:
            queryset = self.queryset.filter(published_at__lte=timezone.now())

        elif not self.request.user.is_staff:
            queryset = self.queryset
        # filter for own or
        else:
            queryset = self.queryset.filter(
                Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
            )

        time_period_name = self.kwargs.get("period_name")
        if not time_period_name:
            # no  further filtering required
            return queryset

        if time_period_name == "new":
            return queryset.filter(
                published_at__gte=timezone.now() - timedelta(hours=1)
            )
        elif time_period_name == "today":
            return queryset.filter(
                published_at__date=timezone.now().date(),
            )
        elif time_period_name == "week":
            return queryset.filter(published_at__gte=timezone.now() - timedelta(days=7))
        else:
            raise Http404(
                f"Time period {time_period_name} is not valid , should be"
                f"'new', 'today' or 'week ' ",
            )

    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @method_decorator(cache_page(2 * 60))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer

    @method_decorator(cache_page(60 * 5))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)

        page = self.paginate_queryset(posts)

        if page is not None:
            serializer = PostSerializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)


