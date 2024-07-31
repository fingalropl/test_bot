from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import TaskListView
from django.conf.urls import url


# v1_router = DefaultRouter()

# v1_router.register('Task', TaskListView)

# urlpatterns = [
#     path('v1/', include(v1_router.urls)),
# ]
urlpatterns = [
    path("task_list/", TaskListView.as_view(), name="task_list"),
]