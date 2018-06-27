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

def effacer(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.delete()
    messages.success(request, ('Contenu effacé!'))
    return redirect('accueil')

def reprendre(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.completed = False
    item.save()
    return redirect('accueil')

def fini(request, liste_id):
    item = Liste.objects.get(pk=liste_id)
    item.completed = True
    item.save()
    return redirect('accueil')