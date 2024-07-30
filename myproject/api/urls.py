from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet


v1_router = DefaultRouter()

v1_router.register('Task', TaskViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]