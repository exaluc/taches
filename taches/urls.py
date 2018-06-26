from django.contrib import admin
from django.urls import path, include
from liste_taches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liste_taches.url')),
]
