from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('domaine/', liste_domaines, name='liste_domaines'),
    path('domaine/add', add_domaine, name='add_domaine'),
    path('domaine/update/<int:id>', update_domaine, name='update_domaine'),
    path('domaine/delete/<int:id>', delete_domaine, name='delete_domaine'),

    path('utilisateur/', liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateur/add/', add_utilisateur, name='add_utilisateur'),
    path('utilisateur/update/<int:id>/', update_utilisateur, name='update_utilisateur'),
    path('utilisateur/delete/<int:id>/', delete_utilisateur, name='delete_utilisateur'),

    path('demande/', liste_demandes, name='liste_demandes'),
    path('demande/add/', add_demande, name='add_demande'),
    path('demande/update/<int:id>/', update_demande, name='update_demande'),
    path('demande/delete/<int:id>/', delete_demande, name='delete_demande'),

    path('login/', utilisateur_login, name='utilisateur_login'),
    path('register/', utilisateur_register, name='utilisateur_register'),
    path('logout/', utilisateur_logout, name='utilisateur_logout')
]
