from django import forms
from .models import *

class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = ['intitule', 'description']
        widgets = {
            'intitule' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer le domaine'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea w-full h-24',
                'placeholder': 'Décrire en quelques mots le domaine',
            })
        }

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'telephone', 'address', 'email', 'password', 'role']
        widgets = {
            'nom' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer le nom'
            }),
            'prenom' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer le prénom'
            }),
            'telephone' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer le numéro de téléphone'
            }),
            'address' : forms.Textarea(attrs={
                'class': 'textarea w-full h-24',
                'placeholder': 'Entrer l\'adresse'
            }),
            'email' : forms.EmailInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer l\'email'
            }),
            'password' : forms.PasswordInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer le mot de passe'
            }),
            'role' : forms.Select(attrs={
                'class': 'select w-full',
            })
        }

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['client', 'technicien', 'domaine', 'intitule', 'description', 'statuts']
        widgets = {
            'client' : forms.Select(attrs={
                'class': 'select w-full',
                'placeholder': 'Sélectionner le client'
            }),
            'technicien' : forms.Select(attrs={
                'class': 'select w-full',
            }),
            'domaine' : forms.Select(attrs={
                'class': 'select w-full',
            }),
            'intitule' : forms.TextInput(attrs={
                'class': 'input w-full',
                'placeholder': 'Entrer l\'intitulé de la demande'
            }),
            'description' : forms.Textarea(attrs={
                'class': 'textarea w-full h-24',
                'placeholder': 'Décrire en quelques mots la demande'
            }),
            'statuts' : forms.Select(attrs={
                'class': 'select w-full',
            })
        }
