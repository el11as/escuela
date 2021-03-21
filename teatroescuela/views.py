from django.shortcuts import render
from django.views.generic import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseServerError
from utilidades.views import *
# Create your views here.

class TeatroEscuela(TemplateView):
    template_name = 'index.html'

class Nosotres(TemplateView):
    template_name = 'about.html'

class Modelo(TemplateView):
    template_name = 'modelo.html'

class Contacto(TemplateView):
    template_name = 'contact.html'

class Facilitadores(TemplateView):
    template_name = 'facilitadores.html'

class Programas(TemplateView):
    template_name = 'programas.html'

class ResgitroView(View):

    def post(self, request, *args, **kwargs):

        try:
            status = True
            message = 'Evio de correo'
            error   = 'Envio de correo exitoso'

            # contacto = Contacto()
            # contacto.nombre   = request.POST.get('a-nombre')
            # contacto.correo   = request.POST.get('a-email')
            # contacto.telefono = request.POST.get('a-phone')
            # contacto.mensaje  = request.POST.get('a-mensaje')
            # contacto.save()

            enviar_mail(
                html = True,
                to_email = ['admision@teatroescuela.cl'],
                subject = 'Nueva Consulta',
                message = 'mail/nuevo-admin.html',
                data = {
                    'nombre'   : request.POST.get('a-nombre'),
                    'email'    : request.POST.get('a-email'),
                    'asunto'   : request.POST.get('a-asunto'),
                    'mensaje'  : request.POST.get('a-mensaje'),
                },
            )

            return JsonResponse({
                'status'  : status,
                'message' : message,
                'error'   : error
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                'status'  : status,
                'message' : message,
                'error'   : str(e)
            }, status = 500)
