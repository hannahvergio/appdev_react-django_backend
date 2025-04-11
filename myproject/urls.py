from django.contrib import admin
from django.urls import path, include
from myapp.views import index
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')), 
    path('', index), 
    path('api-token-auth/', obtain_auth_token),
]