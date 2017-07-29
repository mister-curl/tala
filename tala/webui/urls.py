from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nodes/$', views.node, name='nodes'),
    url(r'^images/$', views.image, name='images'),
]
