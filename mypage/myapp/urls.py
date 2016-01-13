from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'/maps_page', views.maps_page, name='maps_page'),


]