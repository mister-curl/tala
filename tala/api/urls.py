from django.conf.urls import url, include
from rest_framework_nested import routers

from api import views

router = routers.SimpleRouter()
router.register(r'nodes', views.NodeViewSet)
router.register(r'vms', views.VirtualMachineViewSet)
router.register(r'containers', views.ContainersViewSet)
router.register(r'users', views.UserViewSet)


nodes_router = routers.NestedSimpleRouter(router, r'nodes', lookup='node')
nodes_router.register(r'graphs', views.NodeGraphViewSet, base_name='node-graphs')
nodes_router.register(r'metrics', views.MetricsViewSet, base_name='node-metrics')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(nodes_router.urls)),
]
