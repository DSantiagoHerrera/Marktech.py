from django.contrib import admin
from django.urls import path, include
from django.urls import path
from home.views import inicio  # Asegúrate de importar la vista de inicio desde tu aplicación hom


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('', inicio, name='inicio'), 
]
