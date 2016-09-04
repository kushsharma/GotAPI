from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<year_no>[0-9]+)$', views.year, name = "year"),
]
