from django.conf.urls import url, include
from rest_framework_nested import routers

from api import views

router = routers.SimpleRouter()
router.register(r'nodes', views.NodeViewSet)

nodes_router = routers.NestedSimpleRouter(router, r'nodes', lookup='node')
nodes_router.register(r'graphs', views.NodeGraphViewSet, base_name='node-graphs')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(nodes_router.urls)),
]
