from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import Category, Post, Tag
from .forms import CommentForm



from.models import Post, Comment
from.serializers import PostSerializer, CommentSerializer, PostCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .filters import PostFilter
from rest_framework import serializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

class PostList(ListAPIView):
    serializer_class = PostSerializer
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = Post.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(author__username=username)

        print(queryset)

        return queryset


@api_view(['GET'])
def post_comments(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

# def custom_404(request, exception):
#     return render(request, '404.html', status=404)
#
#
# class BlogListView(ListView):
#     model = Post
#     paginate_by = 2
#     template_name = "post/post_list.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['tags'] = Tag.objects.all()
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         search_query = self.request.GET.get('search')
#         category_slug = self.request.GET.get('category')
#         tag_slug = self.request.GET.get('tag')
#
#         if search_query:
#             queryset = queryset.filter(name__icontains=search_query) | queryset.filter(description__icontains=search_query)
#
#         if category_slug:
#             queryset = queryset.filter(category__slug=category_slug)
#
#         if tag_slug:
#             queryset = queryset.filter(tags__slug=tag_slug)
#
#         return queryset
#
#
#
# class PostListByCategoryView(ListView):
#     model = Post
#     template_name = 'post/post_list.html'
#     paginate_by = 2
#
#     def get_queryset(self):
#         category_slug = self.kwargs.get('category_slug')
#         category = get_object_or_404(Category, slug=category_slug)
#         return Post.objects.filter(category=category)
#
#
# class PostListByTagView(ListView):
#     model = Post
#     template_name = 'post/post_list.html'
#     paginate_by = 2
#
#     def get_queryset(self):
#         tag_slug = self.kwargs.get('tag_slug')
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         return Post.objects.filter(tags=tag)
#
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "post/post_detail.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             post = self.get_object()
#             comment = form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect(post.get_absolute_url())
#         return self.get(request, *args, **kwargs)
#
#
# class BlogCreateView(SuccessMessageMixin, CreateView):
#     model = Post
#     template_name = "post/post_new.html"
#     fields = ["name", "description", "featured_image", "category", "tags"]
#
#     success_message = "%(name)s успешно создан"
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class BlogUpdateView(SuccessMessageMixin, UpdateView):
#     model = Post
#     template_name = "post/post_edit.html"
#     fields = ["name", "description", "featured_image", "category", "tags"]
#     success_message = "%(name)s успешно обновлен"
#
#     def dispatch(self, request, *args, **kwargs):
#         post = get_object_or_404(Post, slug=kwargs['slug'])
#         if post.author != request.user:
#             raise PermissionDenied
#         return super().dispatch(request, *args, **kwargs)
#
#
# class BlogDeleteView(DeleteView):
#     model = Post
#     template_name = "post/post_delete.html"
#     success_url = reverse_lazy("post_list")
#
#     def dispatch(self, request, *args, **kwargs):
#         post = get_object_or_404(Post, slug=kwargs['slug'])
#         if post.author != request.user:
#             raise PermissionDenied
#         return super().dispatch(request, *args, **kwargs)

# @api_view(['POST'])
# def create_post(request):
#     serializer = PostCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

