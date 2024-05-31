from django import forms
from .models import Comment, Post
from tinymce.widgets import TinyMCE
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from ckeditor.widgets import CKEditorWidget



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']





# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description']
#         widgets = {
#             'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
#         }

# class CommentForm(forms.ModelForm):
    

#     class Meta:
#         model = Comment
#         fields = ['body']
#         widgets = {
#             'body': TinyMCE(attrs={'cols': 80, 'rows': 30}),
#         }


# class CommentForm(forms.ModelForm):
#     body = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Comment
#         fields = ['body']
#         labels = {
#             'body': 'Комментарий'
#         }