from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


def new(request):
    return render(request, 'todos/new.html')


def create(request):
    title = request.POST['title']
    content = request.POST['content']
    deadline = request.POST['deadline']
    priority = request.POST['priority']

    todo = Todo(title=title, content=content,
                deadline=deadline, priority=priority)
    todo.save()

    context = {
        'todo': todo,
    }

    return redirect('todos:detail', todo.pk)


def delete(request, pk):
    article = Todo.objects.get(pk=pk)
    article.delete()
    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/edit.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')
    deadline = request.POST.get('deadline')
    priority = request.POST.get('priority')

    todo.title = title
    todo.content = content
    todo.deadline = deadline
    todo.priority = priority

    todo.save()
    return redirect('todos:detail', todo.pk)


def toggle(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')
