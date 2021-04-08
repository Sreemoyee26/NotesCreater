from django.db import models

class Note(models.Model):
    text=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

