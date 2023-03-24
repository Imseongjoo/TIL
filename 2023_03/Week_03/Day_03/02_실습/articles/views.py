from django.shortcuts import render
import random


# Create your views here.


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)


def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면']
    menu = random.choice(foods)
    context = {
        'menu': menu,
    }
    return render(request, 'articles/today_dinner.html', context)


def lotto_create(request):
    return render(request, 'articles/lotto_create.html')


def lotto(request):
    count = int(request.GET.get('count'))
    lotto_numbers = []

    for i in range(count):
        lotto_numbers.append(random.sample(range(1, 46), 6))

    context = {
        'lotto_numbers': lotto_numbers,
    }
    return render(request, 'articles/lotto.html', context)
