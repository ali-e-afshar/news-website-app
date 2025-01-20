# news/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsPost, Comment, Like
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def news_list(request):
    news_posts = NewsPost.objects.all()
    return render(request, 'news_list.html', {'news_posts': news_posts})


def news_detail(request, pk):
    news_post = get_object_or_404(NewsPost, pk=pk)
    return render(request, 'news_detail.html', {'news_post': news_post})


@login_required
def add_comment(request, pk):
    news_post = get_object_or_404(NewsPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_post = news_post
            comment.user = request.user
            comment.save()
            news_post.comments_count += 1
            news_post.save()
            return redirect('news_detail', pk=news_post.pk)
    else:
        form = CommentForm()
    return render(request, 'news/add_comment.html', {'form': form, 'news_post': news_post})


@login_required
def like_post(request, pk):
    news_post = get_object_or_404(NewsPost, pk=pk)
    if not news_post.likes_rel.filter(user=request.user).exists():
        Like.objects.create(news_post=news_post, user=request.user)
        news_post.likes += 1
        news_post.save()
    return redirect('news_detail', pk=news_post.pk)
