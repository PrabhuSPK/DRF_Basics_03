from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexapi,name='index'),
    path('login/',views.loginapi,name='login'),

    
  
]