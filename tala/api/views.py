from api.serializers import NodeSerializer
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
