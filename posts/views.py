from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Post, Comment, Replay
from .serializers import PostListSerializer, CommentSerializer, PostDetailSerializer, UserSerializer, CommnetDetailSerialzer, UserDetailSerializer, ReplaySerializer
from posts import permissions


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly,)


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class CommnetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommnetDetailSerialzer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly,)


class ReplayDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Replay.objects.all()
    serializer_class = ReplaySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsAdminOrReadOnly)


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    permission_classes = (IsAdminUser,)


@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'users' : reverse(viewname = 'user-list', request = request, format = format),
        'posts' : reverse(viewname = 'post-list', request = request, format = format),
        'comments' : reverse(viewname = 'comment-list', request = request, format = format),
    })
