from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template("main/index.html")
    return HttpResponse(template.render({}, request))

def htmlPage(request, pageName=None):
    template = loader.get_template("main/" + pageName)
    return HttpResponse(template.render({}, request))


def doesNotExist(request, pageName=None):
    return redirect("/")


