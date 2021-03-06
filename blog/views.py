from django.shortcuts import render, get_object_or_404

# Create your views here.
import markdown
from .models import Post


def index(request):
    # return render(request, 'blog/index.html', context={
    #     'title':'我的博客首页',
    #     'welcome':'欢迎访问我的博客首页'
    # })
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        # 'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code'
    ])
    return render(request, 'blog/detail.html', context={'post': post})
