"""
URL configuration for site_to_check_junior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import converters
from . import views
register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [

    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('addpage/', views.addpage, name='addpage'),
    path('sing-in/', views.sing_in, name='sing-in'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
]
