from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    heading = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    blog_photo = models.ImageField(upload_to='blog_photos/')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading