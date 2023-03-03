from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'imims', views.ImapViewSet)

urlpatterns = [
    path('', include(router.urls)), #post,get,delete 할때 사용
    path('emailauths/', views.ImapView2.as_view()), #메일 인증
    path('imaplists/', views.ImapGetList.as_view()),
    path('imaplists/<int:pk>/', views.FolderGetList.as_view()),
    path('emailauths/<int:pk>/', views.ImapGetView.as_view()), #사용자 정보 조회
    path('tokenemails/', views.TokenGetView.as_view()), #메일 인증
]