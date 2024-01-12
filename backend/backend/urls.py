from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("fundacion/", include("fundacion.urls")),
    path('admin/', admin.site.urls),
]
