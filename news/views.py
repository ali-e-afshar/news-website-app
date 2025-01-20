# news/views.py
from django.shortcuts import render, get_object_or_404
from .models import NewsPost, Comment, Like


def news_list(request):
    news_posts = NewsPost.objects.all()
    return render(request, 'news_list.html', {'news_posts': news_posts})


def news_detail(request, pk):
    news_post = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'news_detail.html', {'news_post': news_post})
