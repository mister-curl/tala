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


class NodeGraphViewSet(BaseLineChartView,
                       viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin):
    node = None
    graph_type = None
    graph_range = None

    def get_labels(self):
        """Return 7 labels for the x-axis."""
        # 1分
        # 1時間
        # 1日
        # 1週間
        return ["January", "February", "March", "April", "May", "June", "July"]

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
            network_incoming = Metrics.objects.filter(node=self.node, metrics_type='network_incoming').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_outgoing = Metrics.objects.filter(node=self.node, metrics_type='network_outgoing').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_incoming = list(network_incoming)
            network_outgoing = list(network_outgoing)
            return [network_incoming, network_outgoing, network_outgoing]
        elif self.graph_type == "memory":
            network_incoming = Metrics.objects.filter(node=self.node, metrics_type='network_incoming').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_outgoing = Metrics.objects.filter(node=self.node, metrics_type='network_outgoing').order_by(
                '-created_date')[:7].values_list('value', flat=True)
            network_incoming = list(network_incoming)
            network_outgoing = list(network_outgoing)
            return [network_incoming, network_outgoing, network_outgoing]


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
