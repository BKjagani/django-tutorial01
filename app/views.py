from django.shortcuts import render, redirect
from .models import Course, User

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.


@login_required
def home(request):
    data = Course.objects.all()
    return render(request, 'home.html', {"data" : data})

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        role = request.POST.get('role')
        
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'signup.html', {'err_msg' : "User already exists"}) 
        elif User.objects.filter(email=email):
            return render(request, 'signup.html', {'err_msg' : "Plase use uniquie Email ID"}) 
        else: 
            User.objects.create_user(username=username, email=email, password=password, city=city, role=role)
        
        return redirect('login')
        
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        isExists = User.objects.filter(username=username)
        if isExists:
            user = authenticate(username=username, password=password)
            if user:
                if user.role == role:    
                    auth_login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'err_msg' : "Please Select Valid Role"})
            else:
                return render(request, 'login.html', {'err_msg' : "Please Provide Valid Details"})
        else:
            return render(request, 'login.html', {'err_msg' : "User does to exists"})
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user:
            new_pass = str(random.randint(1000, 9999))
            user.set_password(new_pass)
            user.save()
            send_mail("New Password", f"Your New Password is {new_pass}", settings.EMAIL_HOST_USER, [email], fail_silently=False)
            return redirect('login')
        else:
            return render(request, 'forgot_password.html', {'err_msg' : "User not Found"})
    return render(request, 'forgot_password.html')