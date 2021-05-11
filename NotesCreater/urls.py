from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name='NotesCreater'
urlpatterns = [
   path('', views.home, name='home'),
   path('profile/', views.NotesProfile, name='profile'),
   path('profile/add/<int:user_id>/',views.add,name='add'),
   path('profile/add/<int:user_id>/result/',views.result,name='result'),
   path('profile/update/<int:id>/', views.update_note,name='update'),
   path('profile/delete/<int:id>/', views.delete_note,name='delete'),
   path('profile/delete/<int:id>/deleteresult',views.delete,name='deleteresult'),
   path('profile/view/<int:id>/', views.view_note,name='view'),
   path('login/',LoginView.as_view(),name='login'),
   path('register/',views.registerView,name='register'),
   path('logout/',LogoutView.as_view(),name='logout'),
]
