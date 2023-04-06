from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')
    post_filter = request.GET.get('sort')
    if post_filter == 'dev':
        posts = Post.objects.filter(category='개발').order_by('-pk')
    elif post_filter == 'cs':
        posts = Post.objects.filter(category='CS').order_by('-pk')
    elif post_filter == 'newtech':
        posts = Post.objects.filter(category='신기술').order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('posts:detail', todo.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            todo = form.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/update.html', context)


@login_required
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')


def dev(request):
    posts = Post.objects.filter(category='개발')
    context = {'posts': posts}
    return render(request, 'posts/dev.html', context)


def cs(request):
    posts = Post.objects.filter(category='CS')
    context = {'posts': posts}
    return render(request, 'posts/cs.html', context)


def newtech(request):
    posts = Post.objects.filter(category='신기술')
    context = {'posts': posts}
    return render(request, 'posts/newtech.html', context)