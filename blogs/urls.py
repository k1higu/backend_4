from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, post_comments, PostCreate
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:post_id>/comments/', post_comments, name='post-comments'),
    path('posts/create/', PostCreate.as_view(), name='create_post'),
]


# from django.urls import path, include
# from .views import (
#     BlogListView,
#     BlogDetailView,
#     BlogCreateView,
#     BlogUpdateView,
#     BlogDeleteView,
#     PostListByCategoryView,
#     PostListByTagView
# )
# from django.contrib.auth import views as auth_views
#
# handler404 = 'blogs.views.custom_404'
#
# urlpatterns = [
#     path("posts/new/", BlogCreateView.as_view(), name="post_new"),
#     path('<slug:slug>/', BlogDetailView.as_view(), name='post_detail'),
#     path('<slug:slug>/edit/', BlogUpdateView.as_view(), name='post_edit'),
#     path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='post_delete'),
#     path('posts/login/', auth_views.LoginView.as_view(), name='login'),
#     path('posts/logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('category/<slug:category_slug>/', PostListByCategoryView.as_view(), name='post_list_by_category'),
#     path('tag/<slug:tag_slug>/', PostListByTagView.as_view(), name='post_list_by_tag'),
#     path('tinymce/', include('tinymce.urls')),
#     # path('ckeditor/', include('ckeditor_uploader.urls')),
#     path("", BlogListView.as_view(), name="post_list"),
# ]
