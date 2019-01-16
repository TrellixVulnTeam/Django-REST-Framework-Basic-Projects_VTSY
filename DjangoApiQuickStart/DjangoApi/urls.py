from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Api.api_urls')),
    path('admin/', admin.site.urls),
]
