"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings # 为mdeditor做准备
from django.conf.urls.static import static # 为mdeditor做准备

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<str:category_name>', views.category, name='category'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('links/', views.links, name='links'),
    path('about/', views.about, name='about'),
    path('tag/<str:tag_name>', views.tag, name='tag'),
    # path('post/<int:post_id>/post_comment/', views.post_comment, name='post_comment'),
    path('search/', include('haystack.urls'), name='search'),
    path('mdeditor/', include('mdeditor.urls')), # mdeditor配置
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # mdeditor配置