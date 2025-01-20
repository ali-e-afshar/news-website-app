from django.db import models
from accounting.models import CustomUser


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    admin_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='published_news')
    likes = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    news_post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    news_post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='likes_rel')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
