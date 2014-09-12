from django.template.context import Context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    context = {"hi": "hi"}
    return render(request, 'home/index.html', context)

def register(request, action="add"):
    if action=="add":
        return render(request, 'home/register.html')
    if action=="return":
        return render(request, 'home/index.html')
    return render(request, 'home/index.html')

