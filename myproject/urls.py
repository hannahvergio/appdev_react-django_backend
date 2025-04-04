from django.contrib import admin
from django.urls import path, include
from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
    path('', index),  # This maps the root URL to the index view
]