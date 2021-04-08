from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Date information', {'fields': ['created']}),
    ]
    

admin.site.register(Note,NoteAdmin)
