
from django.contrib import admin
from django.urls import path, include
from GestionTrabajosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('GestionTrabajosApp.urls')),
]
