from django.shortcuts import render
from .models import Post
import markdown


def index(request):

    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.body = markdown.markdown(post.body)
    return render(request, 'blog/post.html', {'post': post})


def category(request, category_id):
    return render(request, 'blog/index.html')

