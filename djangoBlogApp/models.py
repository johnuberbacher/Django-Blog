from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        # add to Admin
        return self.category_name

    def get_absolute_url(self):
        # return home when done
        # return reverse('article_detail', args=str((self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Default Tagline')
    meta_description = models.CharField(max_length=255, default='Default Meta Description')
    # Delete all blog posts if user account is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article_detail', args=str((self.id)))
        return reverse('home')
