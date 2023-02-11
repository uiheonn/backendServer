from django.urls import path, include
from . import views


urlpatterns = [
    path('imaplists/', views.ImapGetList.as_view()), #메일 리스트
    path('emailauths/', views.ImapView.as_view()), #메일 인증
    path('emailauths/<int:pk>/', views.ImapGetView.as_view()), #사용자 정보 조회
    path('tokenemails/', views.TokenGetView.as_view()), #메일 인증
]