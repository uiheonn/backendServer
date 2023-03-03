from django.urls import path, include
from . import views

urlpatterns = [
    path('myfolders/', views.FolderView.as_view()),
    path('myfolders/<int:pk>/', views.IdFolderView.as_view()),
]