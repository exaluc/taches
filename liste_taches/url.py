from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('effacer/<liste_id>', views.effacer, name="effacer"),
    path('reprendre/<liste_id>', views.reprendre, name="reprendre"),
    path('fini/<liste_id>', views.fini, name="fini"),
    path('modifier/<liste_id>', views.modifier, name="modifier"),
]
