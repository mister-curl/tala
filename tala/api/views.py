import json

from api.serializers import NodeSerializer, UserSerializer
from chartjs.views.lines import BaseLineChartView
from core.models import Node, User
from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.serializers import MetricsSerializer

from core.models import Metrics


class NodeViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    @detail_route(methods=["POST"])
    def status(self, request, pk=None):
        try:
            node = Node.objects.get(id=pk)
            node_status = self.request.data['status']
        except:
            return HttpResponse({"error": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        if node_status == 'KVM_READY':
            node.type = 'KVM'
            node.status = 'READY'
        else:
            node.status = node_status
        node.save()
        return HttpResponse("Status change completed.", status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=["POST"])
    def power(self, request, pk=None):
        try:
            node = Node.objects.get(id=pk)
            node_power = self.request.data['power']
        except:
            return HttpResponse({"error": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        node.power = node_power
        node.save()
        return HttpResponse("Status change completed.", status=status.HTTP_202_ACCEPTED)

    @detail_route(methods=["POST"])
    def ip_address(self, request, pk=None):
        try:
            node = Node.objects.get(id=pk)
            node_ip_address = self.request.data['ip_address']
        except:
            return HttpResponse({"error": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        node.ip_address = node_ip_address
        node.save()
        return HttpResponse("Status change completed.", status=status.HTTP_202_ACCEPTED)


class NodeGraphViewSet(BaseLineChartView,
                       viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin):
    node = None
    graph_type = None
    graph_range = None

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        label_cpu = Metrics.objects.filter(node=self.node, metrics_type='cpu_load_average_1m').order_by(
            '-created_date')[:7].values_list('date', flat=True)
        date_label = list()
        for d in label_cpu:
            date_label.append(d.strftime('%Y-%m-%d %H:%M:%S'))
        return date_label[::-1]

    def get_providers(self):
        if self.graph_type == "network":
            return ["Incoming", "Outgoing"]
        elif self.graph_type == "disk":
            return ["Read", "Write"]
        elif self.graph_type == "cpu":
            return ["1m", "5m", "10m"]
        elif self.graph_type == "memory":
            return ["total", "used", "free"]

    def get_data(self):
        if self.graph_type == "network":
            network_incoming = Metrics.objects.filter(node=self.node, metrics_type='network_incoming').order_by('-created_date')[:7].values_list('value', flat=True)
            network_outgoing = Metrics.objects.filter(node=self.node, metrics_type='network_outgoing').order_by('-created_date')[:7].values_list('value', flat=True)
            network_incoming = list(network_incoming)
            network_outgoing = list(network_outgoing)
            return [network_incoming, network_outgoing]
        elif self.graph_type == "disk":
            network_incoming = Metrics.objects.filter(node=self.node, metrics_type='network_incoming').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_outgoing = Metrics.objects.filter(node=self.node, metrics_type='network_outgoing').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_incoming = list(network_incoming)
            network_outgoing = list(network_outgoing)
            return [network_incoming, network_outgoing]
        elif self.graph_type == "cpu":
            cpu_load_average_1m = Metrics.objects.filter(node=self.node, metrics_type='cpu_load_average_1m').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            cpu_load_average_5m = Metrics.objects.filter(node=self.node, metrics_type='cpu_load_average_5m').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            cpu_load_average_15m = Metrics.objects.filter(node=self.node, metrics_type='cpu_load_average_15m').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            cpu_load_average_1m = list(cpu_load_average_1m)
            cpu_load_average_5m = list(cpu_load_average_5m)
            cpu_load_average_15m = list(cpu_load_average_15m)

            return [cpu_load_average_1m, cpu_load_average_5m, cpu_load_average_15m]
        elif self.graph_type == "memory":
            memory_total = Metrics.objects.filter(node=self.node, metrics_type='memory_total').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            memory_used = Metrics.objects.filter(node=self.node, metrics_type='memory_used').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            memory_free = Metrics.objects.filter(node=self.node, metrics_type='memory_free').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            memory_total = list(memory_total)
            memory_used = list(memory_used)
            memory_free = list(memory_free)
            return [memory_total, memory_used, memory_free]


        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def retrieve(self, request, *args, **kwargs):
        self.node = kwargs['node_pk']
        self.graph_type = kwargs['pk']
        context = super().get_context_data()
        return Response(context)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        try:
            user = User.objects.get(username=self.kwargs['pk'])
            return user
        except:
            try:
                user = User.objects.get(id=self.kwargs['pk'])
                return user
            except:
                return None


class MetricsViewSet(viewsets.ViewSet):

    serializer_class = MetricsSerializer
    queryset = Metrics.objects.all()

    def create(self, request, node_pk):
        data = request.data
        data.update({"node": int(node_pk)})
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, node_pk):
        queryset = Metrics.objects.filter(node=node_pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, node_pk=None):
        # TODO: metrics_typeごとにグラフを返す処理を実装する
        queryset = Metrics.objects.filter(node=node_pk, metrics_type=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
