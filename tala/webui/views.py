from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def node(request):
    return render(request, 'nodes/index.html')


def image(request):
    return render(request, 'images/index.html')