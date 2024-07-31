# from rest_framework import filters as f
# from .serializer import TaskSerializer
# from models.models import Task
# from rest_framework.filters import SearchFilter
# class TaskFilter(filter.FilterSet):
#     queryset = Task.objects.all
#     serializer_class = TaskSerializer
#     filter_backends = [f.SearchFilter]
#     search_fields = ['text']

# # # class TaskFilter(SearchFilter):
# # #     search_param = 'text'