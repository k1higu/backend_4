from rest_framework import serializers
from .models import Post, Tag, Category, Comment
from django.contrib.auth import get_user_model


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['id', 'name', 'description', 'featured_image', 'slug', 'author', 'tags', 'category', 'comments']

    def get_comments(self, obj):
        request = self.context.get('request')
        include_comments = request.query_params.get('include', '').lower() == 'comments'

        if include_comments:
            comments = Comment.objects.filter(post=obj)
            serializer = CommentSerializer(comments, many=True)
            return serializer.data

        return None


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['featured_image', 'slug']

