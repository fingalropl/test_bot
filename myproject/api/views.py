from models.models import Task
from models.models import Chat
# from django_filters.rest_framework import DjangoFilterBackend
from .serializer import TaskSerializer, ChatSerializer
from rest_framework import filters
from rest_framework import generics
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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

class ChatView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        queryset = Chat.objects.all()
        return Response(queryset.values())


#Если edit_marker в джсон ПУТ запросе 1, то токен обновляется до 20-ти
#Если edit_marker в джсон ПУТ запросе 0, то токен уменьшается на одно использование
class TokenEdit(APIView):
    def put(self, request):
        chat=Chat.objects.get(username=request.data.get('username'))
        m = int((request.data.get('m')))
        if m == 0:
            chat.token = chat.token-1
            chat.save()
            return Response(status.HTTP_200_OK)
        elif m == 1:
            chat.token = 20
            chat.save()
            return Response(status.HTTP_200_OK)
        # chat = Chat.objects.filter(username = request.data.get('username'))
        # print(chat.exists())
        # if chat.exists():
        #     print(chat.values().get('token'))
        # else:
        return Response(status.HTTP_400_BAD_REQUEST)


# class ChatDetail(APIView):
