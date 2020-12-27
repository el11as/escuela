from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from teatroescuela.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('teatroescuela.urls'))
]
