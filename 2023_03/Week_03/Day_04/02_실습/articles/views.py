from django.shortcuts import render

# Create your views here.


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    data = request.GET.get('message')

    context = {
        'data': data,
    }
    return render(request, 'articles/catch.html', context)


def number_print(request, number):
    context = {
        'number': number,
    }
    return render(request, 'articles/number_print.html', context)


def calculate(request, number1, number2):
    add = number1 + number2
    sub = number1 - number2
    mul = number1 * number2
    div = number1 // number2

    context = {
        'number1': number1,
        'number2': number2,
        'add': add,
        'sub': sub,
        'mul': mul,
        'div': div,
    }
    return render(request, 'articles/calculate.html', context)
