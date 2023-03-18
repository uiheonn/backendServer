from django.urls import path

from . import views

urlpatterns = [
    path('registers', views.registerView.as_view()),
    path('logins', views.loginView.as_view()),
]
