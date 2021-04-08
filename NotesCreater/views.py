from django.shortcuts import render,redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm

def home(request):
    
    Notes= Note.objects
    template = loader.get_template('note.html')
    context = {'Notes': Notes}

    return render(request, 'note.html', context)

def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('./result')
    else:
        form = NoteForm()

    context = {'form' : form}

    return render(request, 'add.html', context)

def result(request):
        return render(request, 'result.html')
