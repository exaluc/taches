from django.shortcuts import render
from .models import Liste

def accueil(request):
    return render(request, "accueil.html")
