from django.db import models
from django.db.models.signals import post_save
import datetime
from django.utils import timezone

class Note(models.Model):
    name=models.CharField(max_length=20)
    text=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+": "+self.name
    
