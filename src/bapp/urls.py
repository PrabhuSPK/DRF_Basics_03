from django.urls import path
from . import views

urlpatterns = [
    # path('',views.functionname,name='pathname'),
    # path('',views.classname.as_view(),name='pathname'),

    path('', views.index, name='index'),
    path('login', views.login, name='login'),

]

