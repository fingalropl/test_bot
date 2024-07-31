from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)    
    def __str__(self):
        return f'{self.text}, {self.answer}'
    
class Chat(models.Model):
    username = models.CharField(max_length=100, unique=True)
    token = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.username}, {self.token}'