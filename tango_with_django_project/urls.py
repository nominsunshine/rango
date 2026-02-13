from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
]