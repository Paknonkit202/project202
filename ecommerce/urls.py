"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.homepage),
    path('signin',views.signin),
    path('product',views.product),
    path('detail',views.detail),
    path('shopping',views.shopping),
    path('shipping',views.shipping),
    path('payment',views.payment),
    path('thankyou',views.thankyou),
    path('contact',views.contact),
    path('detail1',views.detail1),
    path('shopping1',views.shopping1),
    path('shipping1',views.shipping1),
    path('payment1',views.payment1),
    path('logout',views.logout),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
