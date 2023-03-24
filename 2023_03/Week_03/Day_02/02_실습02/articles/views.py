from django.shortcuts import render


def berners_lee(request):
    return render(request, 'articles/berners_lee.html')
