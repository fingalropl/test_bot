from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import TaskListView, ChatView, TokenEdit, CheckTokenView
# from django.conf.urls import url


# v1_router = DefaultRouter()

# v1_router.register('Task', TaskListView)

# urlpatterns = [
#     path('v1/', include(v1_router.urls)),
# ]
# v1_router = DefaultRouter()
# v1_router.register('user', UserViewSet, basename='user')
urlpatterns = [
    path("task_list/", TaskListView.as_view(), name="task_list"),
    path("user/", ChatView.as_view(), name="user"),
    path("user/token_edit/", TokenEdit.as_view(), name="user"),
    path("user/token_check/", CheckTokenView.as_view(), name="user_detail"),
]