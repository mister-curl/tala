from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Node
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from core.models import VirtualMachine

from core.models import User


def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test/index.html')


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


class VirtualMachinesView(ListView):
    model = VirtualMachine
    template_name = 'tala/virtual_machines/index.html'


class VirtualMachineView(DetailView):
    model = VirtualMachine
    template_name = 'tala/virtual_machines/detail.html'


class UsersView(ListView):
    model = User
    template_name = 'tala/users/index.html'


class UserView(DetailView):
    model = User
    template_name = 'tala/users/detail.html'


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()

from django.views.generic.edit import CreateView
from django.shortcuts import render


class NodeOSInstall(CreateView):
    model = Node
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'news/news_create_success.html', {'news': self.object})
