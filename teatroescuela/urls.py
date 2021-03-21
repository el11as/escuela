from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'teatroescuela'

urlpatterns = [
    path('', views.TeatroEscuela.as_view(), name='teatro_escuela'),
    path('nosotres/', views.Nosotres.as_view(), name='nosotres'),
    path('facilitadores/', views.Facilitadores.as_view(), name='facilitadores'),
    path('modelo/', views.Modelo.as_view(), name='modelo'),
    path('contacto/', views.Contacto.as_view(), name='contacto'),
    path('programas/', views.Programas.as_view(), name='programas'),
    path('contacto/registrar/', views.ResgitroView.as_view(), name='registrar'),
]
