from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls')),
    path('noticias/', include('backend.noticias.urls')),
    path('eventos/', include('backend.eventos.urls')),
    path('laboratorios/', include('backend.laboratorios.urls')),
    path('salas/', include('backend.salas.urls')),
]
