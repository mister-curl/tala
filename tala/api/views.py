import json

from api.serializers import NodeSerializer
from chartjs.views.lines import BaseLineChartView
from core.models import Node
from django.http import HttpResponse
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route


class NodeViewSet(viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin):

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    @detail_route(methods=["POST"])
    def status(self, request, pk=None):
        try:
            node = Node.objects.get(id=pk)
        except:
            return HttpResponse({"error": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        node.status = "READY"
        return HttpResponse("Status change completed.", status=status.HTTP_202_ACCEPTED)


class NodeGraphViewSet(BaseLineChartView,
                       viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin):

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
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        return HttpResponse(json.dumps(super().get_context_data()))
