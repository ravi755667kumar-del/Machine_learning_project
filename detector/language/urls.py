from operator import index
from turtle import home

from django import views
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path("api/predict/", views.predict, name="predict"),
    ]