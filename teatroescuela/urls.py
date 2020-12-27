from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'teatroescuela'

urlpatterns = [
    path('', views.TeatroEscuela.as_view(), name='teatro_escuela'),
    path('nosotres/', views.Nosotres.as_view(), name='nosotres'),
    path('modelo/', views.Modelo.as_view(), name='modelo'),
    path('contacto/', views.Contacto.as_view(), name='contacto'),
]