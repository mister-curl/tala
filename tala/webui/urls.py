from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test_url/$', views.line_chart_json, name='line_chart_json'),

    # Node
    url(r'^nodes/$', views.NodesView.as_view(), name='nodes'),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeView.as_view(), name='node'),
    url(r'^nodes/create/$', views.NodeCreate.as_view(), name='node-create'),
    url(r'^nodes/(?P<pk>[0-9]+)/edit/$', views.NodeUpdate.as_view(), name='node-edit'),
    url(r'^nodes/(?P<pk>[0-9]+)/delete/$', views.NodeDelete.as_view(), name='node-delete'),
    url(r'^nodes/(?P<pk>[0-9]+)/install/$', views.NodeOsInstall.as_view(), name='node-install'),
    url(r'^nodes/(?P<pk>[0-9]+)/kvm/$', views.NodeKvmCreate.as_view(), name='node-kvm'),
    url(r'^nodes/(?P<pk>[0-9]+)/docker/$', views.NodeDockerCreate.as_view(), name='node-docker'),
    url(r'^nodes/(?P<pk>[0-9]+)/on/$', views.NodePowerOn.as_view(), name='node-power-on'),
    url(r'^nodes/(?P<pk>[0-9]+)/off/$', views.NodePowerOff.as_view(), name='node-power-off'),
    url(r'^nodes/(?P<pk>[0-9]+)/restart/$', views.NodePowerRestart.as_view(), name='node-power-restart'),

    # VirtualMachine
    url(r'^containers/$', views.ContainersView.as_view(), name='containers'),
    url(r'^containers/(?P<pk>[0-9]+)/$', views.ContainerView.as_view(), name='container'),
    url(r'^containers/create$', views.ContainersCreateView.as_view(), name='container-create'),
    url(r'^containers/(?P<pk>[0-9]+)/edit/$', views.ContainerUpdate.as_view(), name='container-edit'),
    url(r'^containers/(?P<pk>[0-9]+)/delete/$', views.ContainerDelete.as_view(), name='container-delete'),
    url(r'^containers/(?P<pk>[0-9]+)/on/$', views.VirtualMachinePowerOn.as_view(), name='vm-power-on'),
    url(r'^containers/(?P<pk>[0-9]+)/off/$', views.VirtualMachinePowerOff.as_view(), name='vm-power-off'),
    url(r'^containers/(?P<pk>[0-9]+)/restart/$', views.VirtualMachinePowerRestart.as_view(), name='vm-power-restart'),

    # Container
    url(r'^virtualmachines/create$', views.VirtualMachineCreateView.as_view(), name='virtualmachine-create'),
    url(r'^virtualmachines/$', views.VirtualMachinesView.as_view(), name='virtualmachines'),
    url(r'^virtualmachines/(?P<pk>[0-9]+)/$', views.VirtualMachineView.as_view(), name='virtualmachine'),
    url(r'^virtualmachines/(?P<pk>[0-9]+)/edit/$', views.VirtualMachineUpdate.as_view(), name='virtualmachine-edit'),
    url(r'^virtualmachines/(?P<pk>[0-9]+)/delete/$', views.VirtualMachineDelete.as_view(), name='virtualmachine-delete'),


    url(r'^users/$', views.UsersView.as_view(), name='users'),
    url(r'^users/create/$', views.UserCreate.as_view(), name='user-create'),
    url(r'^users/(?P<pk>[0-9]+)/delete/$', views.UserDelete.as_view(), name='user-delete'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^users/(?P<pk>[0-9]+)/edit/$', views.UserUpdate.as_view(), name='user-edit'),

    url(r'^images/$', views.image, name='images'),
    url(r'^create/$', views.NodeOSInstall.as_view(), name='news-create'),

    url(r'^login/$', auth_views.login, {'template_name': 'tala/auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/ui'}, name='logout'),
]
