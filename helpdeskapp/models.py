from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    roles = [
        ('client', 'Client'),
        ('technicien', 'Technicien'),
        ('administrateur', 'Administrateur')
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=roles, default='client')

    def __str__(self):
        return f"{self.nom} {self.prenom} {(self.role)}"
    
class Domaine(models.Model):
    intitule = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.intitule}"
    
class Demande(models.Model):
    statut = [
        ('en attente', 'En attente'),
        ('en cours', 'En cours'),
        ('terminee', 'Terminée')
    ]

    client = models.ForeignKey(
        Utilisateur,
        on_delete=models.CASCADE,
        related_name = 'client_demandes',
        limit_choices_to={'role': 'client'}
    )

    technicien = models.ForeignKey(
        Utilisateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name = 'technicien_demandes',
        limit_choices_to={'role': 'technicien'}
    )

    domaine = models.ForeignKey(
        Domaine,
        on_delete=models.CASCADE,
        related_name='domaine_demandes'
    )

    intitule = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    statuts = models.CharField(max_length=20, choices=statut, default='en attente')
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intitule} {(self.statuts)}"