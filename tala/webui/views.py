from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Node


def index(request):
    return render(request, 'index.html')


def node(request):
    return render(request, 'nodes/index.html')


def image(request):
    return render(request, 'images/index.html')


class NodesView(ListView):
    model = Node
    template_name = 'nodes/index.html'


class NodeView(DetailView):
    model = Node
    template_name = 'nodes/detail.html'
