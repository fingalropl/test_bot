from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)    
    def __str__(self):
        return f'{self.text}, {self.answer}'