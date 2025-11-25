from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import *

# Create views for Domaine
def liste_domaines(request):
    domaines = Domaine.objects.all()
    return render(request, 'domaine/liste.html', {'domaines': domaines})

def add_domaine(request):
    form = DomaineForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Le domaine a été ajouté avec succès')
            return redirect('liste_domaines')
        else:
            messages.error(request, 'Erreur lors de l\'ajout du domaine')
    return render(request, 'domaine/form.html', {'form': form})

def update_domaine(request, id):
    domaine = get_object_or_404(Domaine, id=id)
    form = DomaineForm(request.POST, instance=domaine)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Le domaine a été mis à jour avec succès')
            return redirect('liste_domaines')
    else:
            form = DomaineForm(instance=domaine)
    return render(request, 'domaine/form.html', {'form': form, 'domaine': domaine})

def delete_domaine(request, id):
    domaine = get_object_or_404(Domaine, id=id)
    if domaine != None and domaine.id > 0:
        domaine.delete()
        messages.success(request, 'Le domaine a été supprimé avec succès')
    else:
        messages.error(request, 'Erreur lors de la suppression du domaine')
    return redirect('liste_domaines')


# Create views for Utilisateur
def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'utilisateur/liste.html', {'utilisateurs': utilisateurs})

def add_utilisateur(request):
    form = UtilisateurForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'utilisateur a été ajouté avec succès')
            return redirect('liste_utilisateurs')
        else:
            messages.error(request, 'Erreur lors de l\'ajout de l\'utilisateur')
    return render(request, 'utilisateur/form.html', {'form': form})
    
def update_utilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateur, id=id)
    form = UtilisateurForm(request.POST, instance=utilisateur)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'utilisateur a été mis à jour avec succès')
            return redirect('liste_utilisateurs')
        else:
            form = UtilisateurForm(instance=utilisateur)
    return render(request, 'utilisateur/form.html', {'form': form, 'utilisateur': utilisateur})
    
def delete_utilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateur, id=id)
    if utilisateur != None and utilisateur.id > 0:
        utilisateur.delete()
        messages.success(request, 'L\'utilisateur a été supprimé avec succès')
    else:
        messages.error(request, 'Erreur lors de la suppression de l\'utilisateur')
    return redirect('liste_utilisateurs')


# Create views for Demande
def liste_demandes(request):
    demandes = Demande.objects.all()
    return render(request, 'demande/liste.html', {'demandes': demandes})

def add_demande(request):
    form = DemandeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'La demande a été ajoutée avec succès')
            return redirect('liste_demandes')
        else:
            messages.error(request, 'Erreur lors de l\'ajout de la demande')
    return render(request, 'demande/form.html', {'form': form})

def update_demande(request, id):
    demande = get_object_or_404(Demande, id=id)
    form = DemandeForm(request.POST, instance=demande)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'La demande a été mise à jour avec succès')
            return redirect('liste_demandes')
        else:
            form = DemandeForm(instance=demande)
    return render(request, 'demande/form.html', {'form': form, 'demande': demande})

def delete_demande(request, id):
    demande = get_object_or_404(Demande, id=id)
    if demande != None and demande.id > 0:
        demande.delete()
        messages.success(request, 'La demande a été supprimée avec succès')
    else:
        messages.error(request, 'Erreur lors de la suppression de la demande')
    return redirect('liste_demandes')
