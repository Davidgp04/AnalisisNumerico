from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('metodos/', views.metodos, name="metodos"),
    path('biseccion/', views.biseccion, name="biseccion"),
]
