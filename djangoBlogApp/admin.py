from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
# Add Category to django DB
admin.site.register(Category)
