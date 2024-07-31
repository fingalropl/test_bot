from models.models import Task
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TaskSerializer
from rest_framework import filters
from rest_framework import generics

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    # filterset_fields = ('task_text',) 
    search_fields = ('text', )
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.accounts.all()
    # def get_queryset(self):
    #     """
    #     This view should return a list of all the purchases for
    #     the user as determined by the username portion of the URL.
    #     """
    #     queryset = Task.objects.all()
    #     text = self.request.query_params.get('text')
        