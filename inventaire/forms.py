# inventaire_fo/forms.py
from django import forms
from .models import Proprietaire, Coordonnees, EquipementActif, FibreOptique, Axe

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['nom', 'axes']  # Ajoutez d'autres champs si nécessaire

class AxesForm(forms.ModelForm):
    class Meta:
        model = Axe
        fields = ['nom']  # Ajoutez d'autres champs si nécessaire

class CoordonneesForm(forms.ModelForm):
    class Meta:
        model = Coordonnees
        fields = ['proprietaire', 'nom_site','latitude', 'longitude']

class EquipementActifForm(forms.ModelForm):
    class Meta:
        model = EquipementActif
        fields = ['proprietaire', 'coord_extremite', 'nom']  # Ajoutez d'autres champs si nécessaire

# Modifiez votre formulaire FibreOptiqueForm(forms.py)
class FibreOptiqueForm(forms.ModelForm):
    class Meta:
        model = FibreOptique
        fields = ['proprietaire', 'coord_extremite_1', 'coord_extremite_2', 'equipement_actif',
                  'type', 'latence', 'bande_passante', 'nombre_de_brin', 'mode_installation',
                  'longueur_exploitable', 'longueur_supportee', 'interfaces_client_dispo',
                  'interfaces_client_exploitable', 'trajet']
    
    def __init__(self, *args, **kwargs):
        super(FibreOptiqueForm, self).__init__(*args, **kwargs)
        # Ajoutez des étiquettes personnalisées pour les champs
        self.fields['proprietaire'].label_from_instance = lambda obj: obj.nom
        self.fields['coord_extremite_1'].label_from_instance = lambda obj: obj.nom_site
        self.fields['coord_extremite_2'].label_from_instance = lambda obj: obj.nom_site
        self.fields['equipement_actif'].label_from_instance = lambda obj: obj.nom
        self.fields['proprietaire'].required = False
        self.fields['equipement_actif'].required = False
        self.fields['latence'].required = False
        self.fields['bande_passante'].required = False
