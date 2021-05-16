from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ( CreateView, FormView, TemplateView)

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password-login")
        username_register = request.POST.get("username_register")
        password_register = request.POST.get("password")
        confirmpassword = request.POST.get("conpassword")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/signin')
        # if password_register==confirmpassword:
        #     if User.objects.filter(username=username_register).exists():
        #         return redirect('/signin')
        #     else:
        #         new_user= User.objects.create_user(username=username_register,password=password_register)
        #         new_user.save()
        #         auth.login(request,new_user)
        #         return redirect('/')
    return render(request,'signin.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def product(request):
    return render(request,'product.html')

def detail(request):
    return render(request,'detail.html')

def shopping(request):
    return render(request,'shopping.html')

def shipping(request):
    return render(request,'shipping.html')

def payment(request):
    return render(request,'payment.html')

def thankyou(request):
    return render(request,'thankyou.html')

def contact(request):
    return render(request,'contact.html')

def detail1(request):
    return render(request,'detail1.html')

def shopping1(request):
    return render(request,'shopping1.html')

def shipping1(request):
    return render(request,'shipping1.html')

def payment1(request):
    return render(request,'payment1.html')


