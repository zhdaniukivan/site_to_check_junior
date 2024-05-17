from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import  render_to_string


menu = [
    {'title': 'About site', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'addpage'},
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Sing in', 'url_name': 'sing-in'},
]

dada_db = [
    {'id': 1, 'title': 'Анджелина Джойли', 'content': 'биография Анджелины Джойли', 'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Actrises'},
    {'id': 2, 'name': "Singers"},
    {'id': 3, 'name': "Sportsman"},
]

# Create your views here.

def index(request):
    data = {
        'title': 'main page',
        'menu': menu,
        'posts': dada_db,
        'cat_selected': 0,

    }
    return render(request, 'test_page/index.html', data)


def show_post(request, post_id):
    return HttpResponse(f'<h1> This page is about post {post_id}')


def addpage(request):
    return HttpResponse('addpage')


def contacts(request):
    return HttpResponse('contacts')


def sing_in(request):
    return HttpResponse('sing-in')


def about(request):
    data = {'title': 'about page'}
    return render(request, 'test_page/about.html', {'title': 'about page', 'menu': menu})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>We can't found the page</h1>" )

def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': dada_db,
        'cat_selected': cat_id,

    }
    return render(request, 'test_page/index.html', context=data)


