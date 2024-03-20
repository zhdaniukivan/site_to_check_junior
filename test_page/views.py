from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('page test')


def categories(request):
    return HttpResponse('<hi>Test to Categories')
