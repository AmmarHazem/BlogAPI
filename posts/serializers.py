from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Replay


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'title', 'published', 'timestamp')
        extra_kwargs = {
            'url': {'view_name': 'post-detail', 'lookup_field': 'slug'}
        }


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(view_name = 'comment-detail', many = True, read_only = True)
    class Meta:
        model = Post
        fields = ('url', 'title', 'content', 'author', 'published', 'timestamp', 'image', 'comments')
        extra_kwargs = {
            'author' : {'lookup_field' : 'username'},
            'url' : {'lookup_field' : 'slug'}
        }


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'post', 'content', 'timestamp')
        extra_kwargs = {
            'post' : {'lookup_field' : 'slug'}
        }


class CommnetDetailSerialzer(serializers.HyperlinkedModelSerializer):
    replies = serializers.HyperlinkedRelatedField(view_name = 'reply-detail', many = True, read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'post' : {'lookup_field' : 'slug'},
            'author' : {'lookup_field' : 'username'}
        }


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')
        extra_kwargs = {
            'url' : {'lookup_field' : 'username'}
        }

    
class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(view_name = 'post-detail', many = True, read_only = True, lookup_field = 'slug')
    # comments = serializers.HyperlinkedRelatedField(view_name = 'comment-detail', many = True, read_only = True)
    class Meta:
        model = User
        fields = ('url', 'username', 'posts')
        extra_kwargs = {
            'url' : {'lookup_field' : 'username'}
        }


class ReplaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Replay
        fields = ('content', 'comment', 'author')
        extra_kwargs = {
            'author' : {'lookup_field' : 'username'},
        }
