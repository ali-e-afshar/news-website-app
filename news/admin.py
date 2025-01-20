# news/admin.py
from django.contrib import admin
from .models import NewsPost, Comment, Like

admin.site.register(NewsPost)
admin.site.register(Comment)
admin.site.register(Like)
