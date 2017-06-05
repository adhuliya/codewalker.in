from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render({}, request))

def htmlpage(request, pagename=None):
    template = loader.get_template("main/" + pagename)
    return HttpResponse(template.render({}, request))



