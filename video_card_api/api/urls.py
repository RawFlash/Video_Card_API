from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url("db", views.db),
    url("clean_data",views.clean_db),
    url("test",views.test),
    url("json",views.json),
    url("",views.main),
    ]
