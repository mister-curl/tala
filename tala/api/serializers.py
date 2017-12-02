from rest_framework import serializers

from core.models import Node, User

from core.models import Metrics

from core.models import VirtualMachine

from core.models import Container


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


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = '__all__'

    host_server = serializers.SerializerMethodField()

    def get_host_server(self, container):
        return container.docker_host.ip_address
