from .models import Category, Navbarmenu, Post, Comment, Tag


def base(request):
    recent_post_list = Post.objects.order_by('-published_time')[:5]

    recent_comment_list = Comment.objects.order_by('-published_time')[:5]

    category_list = Category.objects.all()

    navbarmenu_list = Navbarmenu.objects.all()

    return {
        'recent_post_list': recent_post_list,
        'recent_comment_list': recent_comment_list,
        'category_list': category_list,
        'navbarmenu_list': navbarmenu_list
    }

def search(request):
    tag_list = Tag.objects.all()
    return {
        'tag_list': tag_list
    }