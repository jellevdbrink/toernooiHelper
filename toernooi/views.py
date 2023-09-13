from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("hello word, how ya doing")


def dashboard(request):
    return render(request, 'toernooi/dashboard.html', {
        'ding': 'kakakak'
    })
