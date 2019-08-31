from django.forms import ModelForm, TextInput, Textarea, EmailInput, URLInput
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'author_mail', 'author_url', 'body']
        widgets = {
            'author': TextInput(attrs={'id': 'author',
                                      'class': 'form-control input-control clearfix',
                                      'placeholder': '昵称*'
                                      }),
            'author_mail': EmailInput(attrs={'id': 'mail',
                                             'class': 'form-control input-control clearfix',
                                             'placeholder': '邮箱*',
                                             }),
            'author_url': URLInput(attrs={'id': 'url',
                                          'class': 'form-control input-control clearfix',
                                          'placeholder': '博客地址 (http://)'}),
            'body': Textarea(attrs={'id': 'textarea',
                                    'class': 'form-control',
                                    'placeholder': '说点什么吧'
            })
        }
