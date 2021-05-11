from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def signin(request):
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


