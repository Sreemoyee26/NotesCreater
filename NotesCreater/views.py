from django.shortcuts import render,redirect,get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseNotFound
from .models import Note
from .forms import NoteForm
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from useraccounts.forms import SignUpForm

@login_required(login_url='/login/')
"""

def home(request):
    
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

"""
def login(request):
    return render(request, 'useraccounts/login.html')

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'registration.html', {'form': form})
"""
