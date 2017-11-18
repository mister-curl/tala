from rest_framework import serializers

from core.models import Node, User

from core.models import Metrics

from core.models import VirtualMachine


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'


class VirtualMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualMachine
        fields = '__all__'

    host_server = serializers.SerializerMethodField()

    def get_host_server(self, virtualmachine):
        return virtualmachine.host_server.ip_address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','ssh_public_key', )


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ('metrics_type', 'unit', 'date', 'value', 'node', )
