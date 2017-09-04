from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test_url/$', views.line_chart_json, name='line_chart_json'),
    url(r'^nodes/$', views.NodesView.as_view(), name='nodes'),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeView.as_view(), name='node'),
    url(r'^virtualmachines/$', views.VirtualMachinesView.as_view(), name='virtualmachines'),
    url(r'^virtualmachines/(?P<pk>[0-9]+)/$', views.VirtualMachineView.as_view(), name='virtualmachine'),
    url(r'^images/$', views.image, name='images'),
    url(r'^create/$', views.NodeOSInstall.as_view(), name='news-create')
]
