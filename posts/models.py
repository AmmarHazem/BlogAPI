from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime


def post_img_loc(obj, filename):
    return f'posts/{obj.author}/{datetime.now().strftime("%d-%m-%y")}/{obj.title}/{filename}'

class Post(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    published = models.BooleanField(default = False)
    image = models.ImageField(upload_to = post_img_loc, null = True, blank = True)
    slug = models.CharField(max_length = 255, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp', 'title')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.author.username

    class Meta:
        ordering = ('-timestamp', 'author')


class Replay(models.Model):
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = 'replies')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'replies')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'Replay: {self.author}'

    class Meta:
        ordering = ('-timestamp', 'author')
