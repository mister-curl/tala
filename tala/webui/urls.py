from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test_url/$', views.line_chart_json, name='line_chart_json'),
    url(r'^nodes/$', views.NodesView.as_view(), name='nodes'),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeView.as_view(), name='node'),
    url(r'^virtualmachines/$', views.VirtualMachinesView.as_view(), name='virtualmachines'),
    url(r'^virtualmachines/(?P<pk>[0-9]+)/$', views.VirtualMachineView.as_view(), name='virtualmachine'),
    url(r'^users/$', views.UsersView.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserView.as_view(), name='user'),
    url(r'^users/(?P<pk>[0-9]+)/edit/$', views.UserUpdate.as_view(), name='user-edit'),
    url(r'^images/$', views.image, name='images'),
    url(r'^create/$', views.NodeOSInstall.as_view(), name='news-create'),
    url(r'^login/$', auth_views.login, {'template_name': 'tala/auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/ui'}, name='logout'),
]
