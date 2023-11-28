from django.urls import re_path
from .import views


urlpatterns = [

    re_path(r'^$', views.index_dash, name='index_dash'),
    re_path(r'^dashboard$', views.dashboard, name='dashboard'),
    re_path(r'^skydash$', views.skydash, name='skydash'),
    
]

