from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['text']}),
    ]
    readonly_fields = ['created']

admin.site.register(Note,NoteAdmin)