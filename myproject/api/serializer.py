from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from models.models import Task

class TaskSerializer(serializers.ModelSerializer):
    # text=serializers.SerializerMethodField(read_only=True)
    # print('1')
    # # def get_text(self, obj):
    # #     request = self.context.get('request')
    # #     print(request)
    # #     return Task.objects.filter(text__contains=request).exists()
    
    # def get_text(self, obj):
    #     request = self.context.get('request')
    #     kek = list(Task.objects.filter(text__contains='сколько').values('text'))
    #     print(kek)
    #     print(len(list(kek)))
    #     print(request)
    #     return Task.objects.filter(text__contains='').exists()
    
    class Meta:
        model = Task
        fields = ('text', 'answer')