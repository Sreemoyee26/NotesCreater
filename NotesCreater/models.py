from django.db import models
from django.db.models.signals import post_save

"""
from django.dispatch import receiver
from django.contrib.auth.models import User

class UserProfile(models.Model):
    first_name = models.CharField(max_length=150)
    last_name =  models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    birth_date = models.DateField()
    password = models.CharField(max_length=150)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
    
"""

class Note(models.Model):
    text=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)+": "+self.name
