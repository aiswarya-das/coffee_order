from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="form"),
    path("welcome/", views.welcome, name="welcome"),
    path("message/", views.message, name="message"),



]
