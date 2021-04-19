from django.urls import path
from . import views
#from django.contrib.auth import views as accounts_views

app_name='NotesCreater'
urlpatterns = [
   path('', views.home, name='home'),
   path('add/',views.add,name='add'),
   path('add/result',views.result,name='result'),
   path('update/<int:id>/', views.update_note,name='update'),
   path('delete/<int:id>/', views.delete_note,name='delete'),
   path('delete/<int:id>/deleteresult',views.delete,name='deleteresult'),
   path('view/<int:id>/', views.view_note,name='view'),
]

#   path('logout/', accounts_views.LogoutView.as_view(template_name="useraccounts/login.html"),name='logout'),
#  path('login/', accounts_views.LoginView.as_view(template_name="useraccounts/login.html"),name='login'),
