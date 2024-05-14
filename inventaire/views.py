# from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

import json
from venv import logger
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Proprietaire, Coordonnees,EquipementActif1, ServiceSupporte, Axe,FibreOptique1,Technologie
from .forms import AxesForm, ProprietaireForm, CoordonneesForm, EquipementActifForm, FibreOptiqueForm
#nouvelle version
# views.py

from django.shortcuts import render, get_object_or_404

# def signin(request):
#     if request.method == 'POST':
#         username = request.POST.get('nom')
#         password = request.POST.get('password')

#         # Query the Proprietaire model to find a matching username (nom) and password
#         proprietaire = Proprietaire.objects.filter(nom=username, password=password).first()

#         if proprietaire:
#             # Login successful, perform any additional actions (e.g., set session variables, etc.)
#             return redirect('liste_axes')  # Redirect to the home page after successful login
#         else:
#             # Login failed, display an error message
#             error_message = "Invalid username or password. Please try again."
#             return render(request, 'signin.html', {'error_message': error_message})

#     else:
#         # If it's a GET request, render the login page
#         return render(request, 'signin.html')
    
    
# def signin(request):

#     return render(request, 'signin.html')  # Render the sign-in page template

def map(request, pk):
    
    fibres = get_object_or_404( FibreOptique1, pk=pk)
    
    return render(request, 'map.html',{'fibres': [fibres]} )

# def mapTest(request):
#     fibres = FibreOptique1.objects.all()
#     return render(request, 'mapTest.html',{'fibres': fibres} )

def liste_axes(request):
    axes = Axe.objects.all()
    # print(axes)
    return render(request, 'liste_axes.html', {'axes': axes})

def liste_fibres(request):
    fibres = FibreOptique1.objects.all()
    return render(request, 'liste_fibre.html', {'fibres': fibres})

def home(request):
    return render(request,"choix_sites.html")

def proprietaires_par_axe(request, axe_id):
    axe = Axe.objects.get(id=axe_id)
    axes = Axe.objects.all()  # Récupérer tous les axes pour afficher dans le select
    proprietaires = Proprietaire.objects.filter(axes__id=axe_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        nom = data.get('nom')
        axes_ids = data.get('axes')
        proprietaire = Proprietaire.objects.create(nom=nom)
        proprietaire.axes.set(axes_ids)
        proprietaire.save()
        return JsonResponse({'message': 'Le propriétaire a été ajouté avec succès.'}, status=201)
    return render(request, 'proprietaires_par_axe.html', {'axes': axes, 'proprietaires': proprietaires, 'axe_id': axe_id})

def proprietaire_delete(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, pk=proprietaire_id)
    proprietaire.delete()
    return JsonResponse({'message': 'Propriétaire supprimé avec succès.'})



def axe_new(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nom_axe = data.get('nom')
        axe = Axe.objects.create(nom=nom_axe)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def axe_delete(request, axe_id):
    axe = get_object_or_404(Axe, pk=axe_id)
    axe.delete()
    return JsonResponse({'success': True})

def detail_proprietaire(request, proprietaire_id):
    proprietaire = get_object_or_404(Proprietaire, pk=proprietaire_id)
    axe_id_str = request.GET.get('axe_id')
    axe_id = None
    if axe_id_str:
        try:
            axe_id = int(axe_id_str)
        except ValueError:
            axe_id = None
    
    coordonnees = proprietaire.coordonnees_set.all()
    
    fibres = FibreOptique1.objects.filter(
        coord_extremite_1__axes__id=axe_id
    ) | FibreOptique1.objects.filter(
        coord_extremite_2__axes__id=axe_id
    )
    
    equipements = EquipementActif1.objects.filter(coordonnees__axes__id=axe_id).distinct()
    technologies = Technologie.objects.filter(equipementactif1__coordonnees__axes__id=axe_id).distinct()
    services_supportes = ServiceSupporte.objects.filter(equipementactif1__coordonnees__axes__id=axe_id).distinct()

    context = {
        'proprietaire': proprietaire,
        'coordonnees': coordonnees,
        'fibres': fibres,
        'equipements': equipements,
        'technologies': technologies,
        'services_supportes': services_supportes,
        'proprietaire_id': proprietaire_id,
        'axe_id': axe_id
    }
    
    return render(request, 'detail_proprietaire.html', context)

def ajouter_fibre_optique(request):
    if request.method == 'POST':
        form = FibreOptiqueForm(request.POST, request.FILES)
        if form.is_valid():
            coord_extremite_1_id = form.cleaned_data['coord_extremite_1'].id
            coord_extremite_2_id = form.cleaned_data['coord_extremite_2'].id
            type = form.cleaned_data['type']
            nombre_de_brin = form.cleaned_data['nombre_de_brin']
            mode_installation = form.cleaned_data['mode_installation']
            longueur_exploitable = form.cleaned_data['longueur_exploitable']
            longueur_supportee = form.cleaned_data['longueur_supportee']
            interfaces_client_dispo = form.cleaned_data['interfaces_client_dispo']
            interfaces_client_exploitable = form.cleaned_data['interfaces_client_exploitable']
            trajet = form.cleaned_data['trajet']
            
            coord_extremite_1 = Coordonnees.objects.get(pk=coord_extremite_1_id)
            coord_extremite_2 = Coordonnees.objects.get(pk=coord_extremite_2_id)

            fibre_optique = FibreOptique1(
                coord_extremite_1=coord_extremite_1,
                coord_extremite_2=coord_extremite_2,
                type=type,
                nombre_de_brin=nombre_de_brin,
                mode_installation=mode_installation,
                longueur_exploitable=longueur_exploitable,
                longueur_supportee=longueur_supportee,
                interfaces_client_dispo=interfaces_client_dispo,
                interfaces_client_exploitable=interfaces_client_exploitable,
                trajet=trajet,
            )
            try:
                fibre_optique.save()
            except IntegrityError as e:
                logger.error('Erreur de sauvegarde de FibreOptique1: %s', str(e))
                return HttpResponseServerError('Erreur de sauvegarde. Veuillez réessayer.')
            proprietaire_id = coord_extremite_1.proprietaire.id
            return redirect('detail_proprietaire', proprietaire_id=proprietaire_id)
        else:
            logger.error('Formulaire invalide: %s', form.errors)
            return HttpResponseBadRequest('Le formulaire est invalide. Veuillez vérifier les données et réessayer.')
    else:
        form = FibreOptiqueForm()
    return render(request, 'detail_proprietaire.html', {'form': form})


def supprimer_fibre_optique(request, fibre_optique_id):
    fibre_optique = get_object_or_404(FibreOptique1, pk=fibre_optique_id)
    proprietaire_id = fibre_optique.coord_extremite_1.proprietaire.id
    fibre_optique.delete()
    return redirect('detail_proprietaire', proprietaire_id=proprietaire_id)

def supprimer_fibre_optique(request, fibre_optique_id):
    fibre_optique = get_object_or_404(FibreOptique1, pk=fibre_optique_id)
    proprietaire_id = fibre_optique.coord_extremite_1.proprietaire.id
    fibre_optique.delete()
    return redirect('detail_proprietaire', proprietaire_id=proprietaire_id)


# Vues pour le modèle Proprietaire
def proprietaire_list(request):
    proprietaires = Proprietaire.objects.all()
    return render(request, 'proprietaire_list.html', {'proprietaires': proprietaires})

def proprietaire_new(request):
    if request.method == "POST":
        form = ProprietaireForm(request.POST)
        if form.is_valid():
            proprietaire = form.save(commit=False)
            proprietaire.save()
            return redirect('proprietaire_list')
    else:
        form = ProprietaireForm()
    return render(request, 'proprietaire_edit.html', {'form': form})

def proprietaire_edit(request, pk):
    proprietaire = get_object_or_404(Proprietaire, pk=pk)
    if request.method == "POST":
        form = ProprietaireForm(request.POST, instance=proprietaire)
        if form.is_valid():
            proprietaire = form.save(commit=False)
            proprietaire.save()
            return redirect('proprietaire_list')
    else:
        form = ProprietaireForm(instance=proprietaire)
    return render(request, 'proprietaire_edit.html', {'form': form, 'proprietaire': proprietaire})


# Vues pour le modèle Coordonnees
def coordonnees_list(request):
    coordonnees = Coordonnees.objects.all()
    return render(request, 'coordonnees_list.html', {'coordonnees': coordonnees})

def coordonnees_detail(request, pk):
    coordonnee = get_object_or_404(Coordonnees, pk=pk)
    return render(request, 'coordonnees_detail.html', {'coordonnee': coordonnee})

def coordonnees_new(request):
    if request.method == "POST":
        form = CoordonneesForm(request.POST)
        if form.is_valid():
            coordonnee = form.save(commit=False)
            coordonnee.save()
            return redirect('coordonnees_list')
    else:
        form = CoordonneesForm()
    return render(request, 'coordonnees_edit.html', {'form': form})

def coordonnees_edit(request, pk):
    coordonnee = get_object_or_404(Coordonnees, pk=pk)
    if request.method == "POST":
        form = CoordonneesForm(request.POST, instance=coordonnee)
        if form.is_valid():
            coordonnee = form.save(commit=False)
            coordonnee.save()
            return redirect('coordonnees_list')
    else:
        form = CoordonneesForm(instance=coordonnee)
    return render(request, 'coordonnees_edit.html', {'form': form, 'coordonnee': coordonnee})

def coordonnees_delete(request, pk):
    coordonnee = get_object_or_404(Coordonnees, pk=pk)
    coordonnee.delete()
    return redirect('coordonnees_list')

# Vues pour le modèle EquipementActif

def equipementactif_new(request):
    if request.method == "POST":
        form = EquipementActifForm(request.POST)
        if form.is_valid():
            equipement = form.save(commit=False)
            equipement.save()
            return redirect('equipementactif_list')
    else:
        form = EquipementActifForm()
    return render(request, 'equipementactif_edit.html', {'form': form})

def equipementactif_list(request):
    equipements = EquipementActif.objects.all()
    return render(request, 'equipementactif_list.html', {'equipements': equipements})

def equipementactif_delete(request, pk):
    fibre = get_object_or_404(EquipementActif, pk=pk)
    fibre.delete()
    return redirect('equipementactif_list')

def equipementactif_detail(request, pk):
    equipement = get_object_or_404(EquipementActif, pk=pk)
    return render(request, 'equipementactif_detail.html', {'equipement': equipement})

def equipementactif_edit(request, pk):
    equipement = get_object_or_404(EquipementActif, pk=pk)

    if request.method == "POST":
        form = EquipementActifForm(request.POST, instance=equipement)

        if form.is_valid():
            equipement = form.save(commit=False)
            equipement.save()
            return redirect('equipementactif_list')
    else:
        form = EquipementActifForm(instance=equipement)

    return render(request, 'equipementactif_edit.html', {'form': form, 'equipement': equipement})

#

def fibreoptique_list(request):
    fibres = FibreOptique.objects.all()
    return render(request, 'fibreoptique_list.html', {'fibres': fibres})

def fibreoptique_detail(request, pk):
    fibre = get_object_or_404(FibreOptique, pk=pk)
    return render(request, 'fibreoptique_detail.html', {'fibre': fibre})


# Ajoutez ces lignes à votre vue fibreoptique_new dans views.py
def fibreoptique_new(request):
    if request.method == "POST":
        form = FibreOptiqueForm(request.POST,  request.FILES)
        if form.is_valid():
            fibre = form.save(commit=False)
            # Effectuez des opérations supplémentaires si nécessaire avant de sauvegarder
            fibre.save()
            return redirect('fibreoptique_list')
        else:
            print(form.errors)
    else:
        form = FibreOptiqueForm()

    return render(request, 'fibreoptique_edit.html', {'form': form})


def fibreoptique_edit(request, pk):
    fibre = get_object_or_404(FibreOptique, pk=pk)
    if request.method == "POST":
        form = FibreOptiqueForm(request.POST, request.FILES, instance=fibre)  # Ajoutez request.FILES

        if form.is_valid():
            fibre = form.save(commit=False)
            fibre.save()
            return redirect('fibreoptique_list')
    else:
        form = FibreOptiqueForm(instance=fibre)
    return render(request, 'fibreoptique_edit.html', {'form': form, 'fibre': fibre})

def fibreoptique_delete(request, pk):
    fibre = get_object_or_404(FibreOptique, pk=pk)
    fibre.delete()
    return redirect('fibreoptique_list')