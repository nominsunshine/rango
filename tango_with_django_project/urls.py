from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # This connects /rango/ to rango app urls
    path('rango/', include('rango.urls')),

    # Admin page
    path('admin/', admin.site.urls),
]

# This allows media files (profile images) to work
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)