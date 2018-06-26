from django.shortcuts import render, redirect
from .models import Liste
from .forms import ListeForm
from django.contrib import messages

def accueil(request):
    if request.method == 'POST':
        form = ListeForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Liste.objects.all
            messages.success(request, ('Cotenu ajouté!'))
            return render(request, 'accueil.html', {'all_items': all_items})

    else:
        all_items = Liste.objects.all
        return render(request, 'accueil.html', {'all_items': all_items})        
