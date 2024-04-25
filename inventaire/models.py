# inventaire_fo/models.py
#################"""nouvelle version "
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import FileExtensionValidator
import os
from django.db import models



class Axe(models.Model):
    nom = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nom


class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    axes = models.ManyToManyField(Axe, default=[1])  # Remplacez [1] par une liste des IDs des axes par défaut

    def __str__(self):
        return self.nom
    


class Technologie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class ServiceSupporte(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class EquipementActif1(models.Model):
    nom = models.CharField(max_length=100)
    constructeur = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technologie)
    services_supportes = models.ManyToManyField(ServiceSupporte)

    def __str__(self):
        return self.nom


class Coordonnees(models.Model):
    axes = models.ForeignKey(Axe, on_delete=models.CASCADE, null=True, blank=True)  # Remplacez [1] par une liste des IDs des axes par défaut
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE, null=True, blank=True)
    nom_site = models.CharField(max_length=255)
    longitude = models.FloatField(validators=[MinValueValidator(-50), MaxValueValidator(50)])
    latitude = models.FloatField(validators=[MinValueValidator(-50), MaxValueValidator(50)])
    equipement = models.ManyToManyField(EquipementActif1)


    def __str__(self):
        #return self.nom_site
        return f"{self.nom_site} - Propriétaire: {self.proprietaire.nom if self.proprietaire else 'Non défini'} - Axe: {self.axes.nom if self.axes else 'Non défini'}"


def upload_json_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    nom_site_extremite_1 = instance.coord_extremite_1.nom_site
    nom_site_extremite_2 = instance.coord_extremite_2.nom_site
    return f'json/{nom_site_extremite_1}_{nom_site_extremite_2}_{instance.id}.json'

class FibreOptique1(models.Model):
    coord_extremite_1 = models.ForeignKey(Coordonnees, related_name='extremite_1_fibre', on_delete=models.CASCADE)
    coord_extremite_2 = models.ForeignKey(Coordonnees, related_name='extremite_2_fibre', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    nombre_de_brin = models.IntegerField()
    mode_installation = models.CharField(max_length=255)
    longueur_exploitable = models.FloatField()
    longueur_supportee = models.FloatField()
    interfaces_client_dispo = models.IntegerField()
    interfaces_client_exploitable = models.IntegerField()
    trajet = models.FileField(upload_to=upload_json_path, validators=[FileExtensionValidator(['json'])], blank=True, null=True)  

    def __str__(self):
        return f"FibreOptique {self.id}"

















    ###################1ére version##################



class EquipementActif(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    #coord_extremite = models.OneToOneField(Coordonnees, related_name='extremite', on_delete=models.CASCADE)
    coord_extremite = models.ForeignKey(Coordonnees, on_delete=models.CASCADE)

    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    # Ajoutez d'autres champs pour les informations de l'équipement actif

"""class FibreOptique(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    coord_extremite_1 = models.OneToOneField(Coordonnees, related_name='extremite_1', on_delete=models.CASCADE)
    coord_extremite_2 = models.OneToOneField(Coordonnees, related_name='extremite_2', on_delete=models.CASCADE)
    equipement_actif = models.OneToOneField(EquipementActif, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    latence = models.FloatField()
    bande_passante = models.FloatField()
    nombre_de_brin = models.IntegerField()
    mode_installation = models.CharField(max_length=255)
    longueur_exploitable = models.FloatField()
    longueur_supportee = models.FloatField()
    interfaces_client_dispo = models.IntegerField()
    interfaces_client_exploitable = models.IntegerField()
    # Ajoutez d'autres champs pour les informations de la fibre optique
"""

# Modifiez votre modèle FibreOptique(models.py)
class FibreOptique(models.Model):
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    coord_extremite_1 = models.ForeignKey(Coordonnees, related_name='extremite_1', on_delete=models.CASCADE)
    coord_extremite_2 = models.ForeignKey(Coordonnees, related_name='extremite_2', on_delete=models.CASCADE)
    equipement_actif = models.ForeignKey(EquipementActif, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    latence = models.FloatField()
    bande_passante = models.FloatField()
    nombre_de_brin = models.IntegerField()
    mode_installation = models.CharField(max_length=255)
    longueur_exploitable = models.FloatField()
    longueur_supportee = models.FloatField()
    interfaces_client_dispo = models.IntegerField()
    interfaces_client_exploitable = models.IntegerField()
    trajet = models.FileField(upload_to='trajets/', blank=True, null=True)  # Ajout de la nouvelle colonne trajet

    # Ajoutez d'autres champs pour les informations de la fibre optique

    def __str__(self):
        return f"FibreOptique {self.id}"
