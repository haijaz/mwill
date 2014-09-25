from django.template.context import Context
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from sitegate.decorators import sitegate_view

def index(request):
    context = {"hi": "hi"}
    return render(request, 'home/index.html', context)

@sitegate_view
def register(request, action="add"):

    if action=="asdfd":
        return render(request, 'home/register.html')
    if action=="asdfdsa":
        return render(request, 'home/index.html')
    return render(request, 'home/register.html', {'title': 'Sign in & Sign up'})

def index(request):
    return render(request, "home/test.html")