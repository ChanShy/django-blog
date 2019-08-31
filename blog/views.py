from django.shortcuts import render, HttpResponseRedirect, Http404
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from .models import Post, Tag, Category, Comment
from .forms import CommentForm

from urllib.parse import unquote

import markdown


def index(request):

    post_list = Post.objects.all()
    paginator = Paginator(post_list, 5)

    if request.method == 'GET':
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except InvalidPage:
            return Http404()
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'post_list': post_list})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.body = markdown.markdown(post.body)

    parent_comment_list = post.comment_set.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 1.模型中添加  2.重定向到评论本身
            author = form.cleaned_data['author']
            author_mail = form.cleaned_data['author_mail']
            author_url = form.cleaned_data['author_url']
            body = form.cleaned_data['body']
            c = Comment.objects.create(author = author, author_mail=author_mail,
                                       author_url=author_url, body=body, post=Post.objects.get(id=post_id))
            return HttpResponseRedirect(reverse('post', args=[str(post_id)]))
    else:
        form = CommentForm() # get请求时返回空表单
    return render(request, 'blog/post.html', {'post': post, 'form': form,
                                              'parent_comment_list': parent_comment_list})


def category(request, category_name):
    category_name = unquote(category_name)
    category = Category.objects.get(name=category_name)
    post_list = category.post_set.all()
    return render(request, 'blog/category.html', {'post_list': post_list})

def links(request):
    return render(request, 'blog/links.html')

def about(request):
    return render(request, 'blog/about.html')

def tag(request, tag_name):
    tag_name = unquote(tag_name)
    tag = Tag.objects.get(name=tag_name)
    post_list = tag.post_set.all()
    return render(request, 'blog/tag.html', {'post_list': post_list})