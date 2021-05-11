from django.db import models
from django.db.models.signals import post_save
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Note(models.Model):
    name=models.CharField(max_length=20)
    text=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="note", null=True)
    def __str__(self):
        return str(self.id)+": "+self.name
