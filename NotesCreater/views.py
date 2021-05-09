from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseNotFound
from .models import Note
from .forms import NoteForm
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'index.html')


@login_required(login_url='/login/')
def NotesProfile(request):
    
    entries = Note.objects.order_by('created')
    context = {'entries' : entries}

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

def update_note(request, id):
  try:
      note = Note.objects.get(id=id)
  except:
      return HttpResponseNotFound("Not Found")
  else:
      if request.method=='GET':
          form = NoteForm(instance=note)
          return render(request,'update.html',{'form':form})
      else:
          note.text=request.POST['text']
          note.name=request.POST['name']
          note.save()
          return redirect('../../')

def delete_note(request, id):
  try:
      note = Note.objects.get(id=id)
  except:
      return HttpResponseNotFound("Not Found")
  else:
      note.delete()
      return redirect('./deleteresult')

def view_note(request,id):
    try:
        note = Note.objects.get(id=id)
    except:
        return HttpResponseNotFound("Not Found")
    else:
        return render(request,'view.html',{'note':note})


def delete(request, id):
        return render(request, 'delete.html')


def registerView(request):
    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect ('../../notes/login')
    else:
        forms = UserCreationForm()

    return render(request, 'registration/register.html',{'forms':forms})
