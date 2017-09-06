from rest_framework import serializers

from core.models import Node, User

from core.models import Metrics


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','ssh_public_key', )


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ('metrics_type', 'unit', 'date', 'value', 'node', )
