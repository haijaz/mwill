from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    context = {"hi": "hi"}
    return render(request, 'home/index.html', context)