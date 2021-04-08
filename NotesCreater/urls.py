from django.urls import path

from . import views

app_name='NotesCreater'
urlpatterns = [
   path('', views.home, name='home'),
   path('add/',views.add,name='add'),
   path('add/result',views.result,name='result')
]