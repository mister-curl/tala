from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nodes/$', views.NodesView.as_view(), name='nodes'),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeView.as_view(), name='node'),
    url(r'^images/$', views.image, name='images'),
]
