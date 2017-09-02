from rest_framework import viewsets

from core.models import Node

from api.serializers import NodeSerializer


class NodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
