from django.urls import path

from . import views

urlpatterns = [
    path('registers', views.createUser),
    path('logins', views.login),
]
