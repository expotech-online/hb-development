from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

class Post(models.Model):
    title = models.CharField(max_length=255)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/%y/%m/%d', default="default.jpg")
    updated_at = models.DateTimeField(default=timezone.now)

    # SEO Fields
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(max_length=255, null=True, blank=True)
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.CharField(max_length=255, null=True, blank=True)
    og_image = models.ImageField(upload_to='seo_images/', null=True, blank=True)
    og_type = models.CharField(max_length=50, default='article')

    def __str__(self):
        return self.title + ' | ' + str(self.auther)
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
    

