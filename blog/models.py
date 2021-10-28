from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	likes = models.ManyToManyField('auth.User', related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',args=(str(self.id)))

	