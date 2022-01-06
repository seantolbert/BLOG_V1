from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {
        'posts': posts
    })

def index(request):
    posts = Post.objects.all().order_by("-date")
    num_posts = posts.count()
    return render(request, "blog/all-posts.html", {
        "posts": posts,
        "total_number_of__posts": num_posts,
    })

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/details.html', {
        'title': post.title,
        'author': post.author,
        "content": post.content,
        "date": post.date

    })
