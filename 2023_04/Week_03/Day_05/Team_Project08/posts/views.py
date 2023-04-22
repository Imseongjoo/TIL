from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.conf import settings
import os


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    user1 = post.select1_users.all()
    user2 = post.select2_users.all()
    if request.user not in user1 and request.user not in user2:
        if answer == 'select1':
            post.select1_users.add(request.user)
        elif answer == 'select2':
            post.select2_users.add(request.user)

    return redirect('posts:detail', post.pk)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm()
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if post.image1:
            image1_path = os.path.join(settings.MEDIA_ROOT, str(post.image1))
            if os.path.isfile(image1_path):
                os.remove(image1_path)
        if post.image2:
            image2_path = os.path.join(settings.MEDIA_ROOT, str(post.image2))
            if os.path.isfile(image2_path):
                os.remove(image2_path)
        post.delete()
    return redirect('posts:index')


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user != post.user:
        return redirect('posts:index')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        print(request.FILES)
        if request.FILES.get('image1', None) != None:
            image1_path = os.path.join(settings.MEDIA_ROOT, str(post.image1))
            if os.path.isfile(image1_path):
                os.remove(image1_path)
        if request.FILES.get('image2', None) != None:
            image2_path = os.path.join(settings.MEDIA_ROOT, str(post.image2))
            if os.path.isfile(image2_path):
                os.remove(image2_path)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/update.html', context)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', post.pk)
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('posts:detail', post_pk)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post.pk)


@login_required
def comment_likes(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('posts:detail', post_pk)
