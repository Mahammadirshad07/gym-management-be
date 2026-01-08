from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls), # Built-in superuser panel
    path('api/', include('api.urls')),      # Your custom endpoints
]
