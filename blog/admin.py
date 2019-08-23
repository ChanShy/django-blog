from django.contrib import admin

from .models import Post, Category, Navbarmenu, Tag, Comment


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Navbarmenu)
admin.site.register(Tag)
admin.site.register(Comment)
