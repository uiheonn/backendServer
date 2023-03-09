from django.urls import path, include
from . import views

urlpatterns = [
    path('keywords/', views.KeywordView.as_view()),
    path('keywords/<int:pk>/', views.DeleteView.as_view()),
]