from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm

from django.http import HttpResponse
from django.contrib.auth.models import User
import jwt
import time

# Create your views here.
# Home page
def index(request):
    return render(request, 'home.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_autologin(request):

    minutes_of_link_active = 1

    encoded_jwt = request.GET.get('t', '')
    if not encoded_jwt == '':
        try:
            decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
        except:
            return HttpResponse("generic error.", status=404)
    else: 
        return HttpResponse("Link is no longer valid.", status=404)

    username = decoded_jwt["user"]

    if int(time.time()) < minutes_of_link_active * 60 + decoded_jwt["time"]:

        try:
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('home')
        except User.DoesNotExist:
            return HttpResponse("User does not exist.", status=404)
    else:
        return HttpResponse("Link is no longer valid.", status=404)


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
