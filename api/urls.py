from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url("json",views.json),
    url("full_db",views.full),
    ]
