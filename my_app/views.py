import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_CRAIGLIST_URL = 'https://losangeles.craigslist.org/search/bbb?query={}'
# Create your views here.

def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    # print(final_url)
    respose = requests.get(final_url)
    data = respose.text
    # print(data)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
