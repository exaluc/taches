from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('effacer/<liste_id>', views.effacer, name="effacer"),
]
