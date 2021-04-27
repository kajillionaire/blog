from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(get_user_model(),on_delete= models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_details', args=[str(self.id)])



class Comment(models.Model): 
    Blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name= 'comments')
    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')

class random:
    pass
# Create your models here.
