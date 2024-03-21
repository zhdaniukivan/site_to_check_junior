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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import converters
from . import views
register_converter(converters.FourDigitYearConverter, 'year4')
urlpatterns = [

    path('', views.index, name='home'),
    path('cat/<int:cat_id>/', views.categories, name='cat_id'),
    path('cat/<slug:cat_slug>/', views.categories_by_slug, name='cat_slug'),
    path('archive/<year4:year>/', views.categories_by_year, name='archive')
]