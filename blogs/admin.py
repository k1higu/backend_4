from django.contrib import admin
from .models import Category, Tag, Post, Comment
# from tinymce.widgets import TinyMCE
# from django.db import models


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)


# Register your models here.
