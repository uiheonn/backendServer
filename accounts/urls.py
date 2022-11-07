from django.urls import path

from . import views

urlpatterns = [
    path('', views.createUser),
    path('login/', views.login),
]