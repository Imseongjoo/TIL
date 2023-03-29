from django.shortcuts import render
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
    title = request.GET.get('title')
    content = request.GET.get('content')
    deadline = request.GET.get('deadline')
    priority = request.GET.get('priority')

    todo = Todo(title=title, content=content,
                deadline=deadline, priority=priority)
    todo.save()

    context = {
        'todo': todo,
    }

    return render(request, 'todos/create.html', context)
