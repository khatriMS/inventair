# admin.py
from django.contrib import admin
from .models import Axe, Proprietaire,Technologie,ServiceSupporte,EquipementActif1,Coordonnees,FibreOptique1

admin.site.register(Axe)
admin.site.register(Proprietaire)
admin.site.register(Technologie)
admin.site.register(ServiceSupporte)
admin.site.register(EquipementActif1)
admin.site.register(Coordonnees)
admin.site.register(FibreOptique1)
# Register your models here.
