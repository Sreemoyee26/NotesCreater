from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext, loader, response
from django.http import HttpResponse,HttpResponseNotFound
from .models import Note
from .forms import NoteForm
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def home(response):
    return render(response,'index.html')


@login_required(login_url='/login/')
def NotesProfile(response):
    
    entries = Note.objects.order_by('created')
    context = {'entries' : entries}

    return render(response, 'note.html', context)

def add(response,user_id):
    if response.method == 'POST':
        user = User.objects.get(pk=user_id)
        form = NoteForm(response.POST)
        
        if form.is_valid():
            #form.save()
            n = form.cleaned_data["name"]
            t = form.cleaned_data["text"]
            entry = Note(name=n,text=t)
            entry.save()
            response.user.note.add(entry)
            return redirect('./result')
    else:
        form = NoteForm()

    context = {'form' : form}

    return render(response, 'add.html', context)

def result(response,user_id):
        return render(response, 'result.html')

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


def registerView(response):
    if response.method == "POST":
        forms = UserCreationForm(response.POST)
        if forms.is_valid():
            forms.save()
            return redirect ('../../notes/login')
    else:
        forms = UserCreationForm()

    return render(response, 'registration/register.html',{'forms':forms})
