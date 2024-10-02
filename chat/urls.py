from django.contrib import admin
from django.urls import path,include

from .views import home,login1,register,chat_person,main,logout1
urlpatterns = [
    path('',main,name='main'),
    path('home/', home , name='home'),
    path('login/', login1, name='login'),
    path('logout/', logout1, name='logout'),
    path('register/', register, name='register'),
    path('chat_person/<int:pk>', chat_person, name = 'chat_person'),

]

