from django.shortcuts import render, redirect
from .models import AccountBook
# Create your views here.


def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)


def detail(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST['note']
    description = request.POST['description']
    category = request.POST['category']
    amount = request.POST['amount']
    date = request.POST['date']

    accountbook = AccountBook(
        note=note, description=description, category=category, amount=amount, date=date)
    accountbook.save()

    return redirect('accountbooks:detail', accountbook.pk)


def edit(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/edit.html', context)


def update(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.note = request.POST['note']
    accountbook.description = request.POST['description']
    accountbook.category = request.POST['category']
    accountbook.amount = request.POST['amount']
    accountbook.date = request.POST['date']

    accountbook.save()

    return redirect('accountbooks:detail', accountbook.pk)


def delete(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.delete()
    return redirect('accountbooks:index')


def copy(request, pk):
    accountbook = AccountBook.objects.get(pk=pk)
    accountbook.pk = None
    accountbook.save()
    return redirect('accountbooks:index')
