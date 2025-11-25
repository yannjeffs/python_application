from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(Utilisateur)
admin.site.register(Domaine)
admin.site.register(Demande)