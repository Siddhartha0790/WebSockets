from django.shortcuts import render,redirect
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views import View
from .forms import Registerform
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Messages
# Create your views here.
from django.contrib import messages
@login_required()
def home(request):
    users = User.objects.all()
    return render(request , 'chats/home.html', {'users': users})

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        username = User.objects.get(username=username)
        if username is not None:
            
           user = authenticate(request, username=username, password=password)
           
        else :
            messages.error(request , 'username dont exist')
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'chats/login.html')

def register(request):
    form = Registerform()
    if request.method == 'POST':
        form = Registerform(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request , 'chats/register.html', {'form':form})

def chat_person(request,pk):
    otheruser = User.objects.get(id=pk)
    
    All_message = Messages.objects.filter(Q(from_user = request.user , to_user = otheruser) | Q(from_user = otheruser , to_user= request.user)).order_by('time')
    return render(request ,'chats/chat_person.html',{'otheruser':otheruser , 'messages':All_message})


def main(request):
    
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'chats/main.html')
    
def logout1(request):
    logout(request)
    return redirect('main')