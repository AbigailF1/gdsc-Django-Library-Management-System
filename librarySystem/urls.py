from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='librarySystem'),
    path('index/', views.index, name='index'),
    path('staff/', views.staff, name='staff'),
]