from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, LoginAPIView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login', LoginAPIView.as_view(), name='api_login'),
] 