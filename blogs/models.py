from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from transliterate import translit
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField



class Comment(models.Model):
    body = models.TextField(verbose_name="Текст комментария")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Автор")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
    body = HTMLField()


    def __str__(self):
        return f"Комментарий к {self.post.name}"


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        r = self.name
        self.slug = slugify(translit(r, 'ru', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        r = self.name
        self.slug = slugify(translit(r, 'ru', reversed=True))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




# class Comment(models.Model):
#     body = models.TextField(verbose_name="Текст комментария",blank=True, null=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="Автор")
#     post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', verbose_name="Пост")
#     # body = RichTextField()


#     def __str__(self):
#         return f"Комментарий к {self.post.name}"

class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    description = RichTextField()
    featured_image = models.ImageField(blank=True, default="default.jpg", upload_to="img/")
    slug = models.SlugField(unique=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    tags = models.ManyToManyField(Tag, related_name='posts', verbose_name="Теги")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', verbose_name="Категория")

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


    def save(self, *args, **kwargs):
        r = self.name
        self.slug = slugify(translit(r, 'ru', reversed=True))
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}"




# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
# class Post(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     featured_image = models.ImageField(upload_to='featured_images/', null=True, blank=True)
#     slug = models.SlugField(unique=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     tags = models.ManyToManyField(Tag, related_name='posts')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.name
#
# class Comment(models.Model):
#     body = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Comment by {self.author} on {self.post}'
