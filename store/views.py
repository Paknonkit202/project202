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
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request,'homepage.html')
    return render(request,'signin.html')

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


