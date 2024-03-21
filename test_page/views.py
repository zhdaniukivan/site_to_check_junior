from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def index(request):
    return HttpResponse('page test')


def categories(request, cat_id):
    return HttpResponse(f"<h1>Test to Categories</h1><p>cat_id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Test to Categories</h1><p>cat_slug: {cat_slug}</p>")


def categories_by_year(request, year):
    if year >2024:
        raise Http404()
    if year < 1850:
        uri = reverse('cat_slug', args=('music', ))
        return redirect(uri)
    if year ==2008:
        return HttpResponseRedirect('/')
        # return redirect('test_page/', permanent=True)
    return HttpResponse(f"<h1>Test to Categories</h1><p>year: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>We can't found the page</h1>" )

