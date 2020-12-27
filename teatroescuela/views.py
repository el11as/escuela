from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError

# Create your views here.

class TeatroEscuela(TemplateView):
    template_name = 'index.html'

class Nosotres(TemplateView):
    template_name = 'about.html'

class Modelo(TemplateView):
    template_name = 'blog.html'

class Contacto(TemplateView):
    template_name = 'contact.html'