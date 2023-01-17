from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dummy', views.BoardViewSet)
router.register(r'keyword', views.KeywordViewSet)
router.register(r'filter', views.FilterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]