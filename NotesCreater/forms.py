from django import forms
from .models import Note

"""
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from useraccounts.models import UserProfile

 class SignUpForm(UserCreationForm):

    class Meta:
        model = User

        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2', )

"""

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ()
