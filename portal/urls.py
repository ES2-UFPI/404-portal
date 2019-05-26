from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls')),
    path('noticias/', include('backend.noticias.urls')),
    path('eventos/', include('backend.eventos.urls')),
    path('feedbacks/', include('backend.feedbacks.urls')),
    path('laboratorios/', include('backend.laboratorios.urls')),
    path('salas/', include('backend.salas.urls')),
    path('reservas/', include('backend.reservas.urls')),
    path('usuarios/', include('backend.usuarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)