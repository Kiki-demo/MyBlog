# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from users.models import User
from .models import Comment
from .forms import CommentForm


# Create your views here.
def post_comment(request, post_pk):
    if not request.session.get('is_login', None):
        # 如果没有登录过，那么给出提示，让其登录后再评论
        print(u'请登录后再来评论')
    user_pk = request.session.get('user_id', -1)
    # user = get_object_or_404(User, pk=user_pk)
    user = get_object_or_404(User, pk=1)  # 因为还没做登录关联，所以，暂时写死登录者
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)
