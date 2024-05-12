from  django.urls import path 
from . import views

urlpatterns=[
    path('signin/', views.signin, name='signin'),
    path('map/<int:pk>/',views.map,name='map'),
    path('',views.home,name="home"),
    path('axes/', views.liste_axes, name='liste_axes'),
    path('axes/new/', views.axe_new, name='axes_new'),
    path('axes/<int:axe_id>/delete/', views.axe_delete, name='axe_delete'),
    path('fibres/', views.liste_fibres, name='liste_fibres'),
    # path('proprietaires/<int:axe_id>/', views.proprietaires_par_axe, name='proprietaires_par_axe'),
    path('proprietaires/<int:axe_id>/', views.proprietaires_par_axe, name='proprietaires_par_axe'),
    path('proprietaires/<int:proprietaire_id>/delete/', views.proprietaire_delete, name='proprietaire_delete'),
    path('ajouter_fibre_optique/', views.ajouter_fibre_optique, name='ajouter_fibre_optique'),
    path('proprietaire/<int:proprietaire_id>/', views.detail_proprietaire, name='detail_proprietaire'),
    # path('supprimer_fibre_optique/<int:fibre_optique_id>/', views.supprimer_fibre_optique, name='supprimer_fibre_optique'),
    # path('supprimer_fibre_optique/', views.supprimer_fibre_optique, name='supprimer_fibre_optique'),
    path('supprimer_fibre_optique/<int:fibre_optique_id>/', views.supprimer_fibre_optique, name='supprimer_fibre_optique'),
    #path('proprietaire/', views.detail_proprietaire, name='detail_proprietaire'),
    #path('proprietaires/<int:proprietaire_id>/<int:axe_id>/', views.detail_proprietaire, name='detail_proprietaire'),
    #path('ajouter-cable/', add_cable, name='ajouter_cable'),
    #path('liste-cables/', list_cables, name='liste_cables'),
    # URLs pour Proprietaire
    path('proprietaires/', views.proprietaire_list, name='proprietaire_list'),
    # path('proprietaires/<int:pk>/', views.proprietaire_detail, name='proprietaire_detail'),
    # path('proprietaires/<int:axe_id>/', views.liste_proprietaires_par_axe, name='liste_proprietaires_par_axe'),
    path('proprietaires/new/', views.proprietaire_new, name='proprietaire_new'),
    # path('ajouter_proprietaire/', views.ajouter_proprietaire, name='ajouter_proprietaire'),
   # path('proprietaires_par_axe/', views.proprietaires_par_axe, name='proprietaires_par_axe'),
    path('proprietaires_par_axe/', views.proprietaires_par_axe, name='proprietaires_par_axe'),
    path('proprietaires/<int:pk>/edit/', views.proprietaire_edit, name='proprietaire_edit'),
    # path('proprietaires/<int:pk>/delete/', views.proprietaire_delete, name='proprietaire_delete'),

    # URLs pour Coordonnees
    path('coordonnees/', views.coordonnees_list, name='coordonnees_list'),
    path('coordonnees/<int:coordonnees_id>/', views.coordonnees_detail, name='coordonnees_detail'),
    path('coordonnees/new/', views.coordonnees_new, name='coordonnees_new'),
path('edit_coordonnees/<int:coordonnees_id>/', views.coordonnees_edit, name='edit_coordonnees'),
    path('coordonnees/<int:pk>/delete/', views.coordonnees_delete, name='coordonnees_delete'),

    # URLs pour EquipementActif
    path('equipements/', views.equipementactif_list, name='equipementactif_list'),
    path('equipements/<int:pk>/', views.equipementactif_detail, name='equipementactif_detail'),
    path('equipements/new/', views.equipementactif_new, name='equipementactif_new'),
    path('equipements/<int:pk>/edit/', views.equipementactif_edit, name='equipementactif_edit'),
    path('equipements/<int:pk>/delete/', views.equipementactif_delete, name='equipementactif_delete'),

    # URLs pour FibreOptique
    path('fibres/', views.fibreoptique_list, name='fibreoptique_list'),
    path('fibres/<int:pk>/', views.fibreoptique_detail, name='fibreoptique_detail'),
    path('fibres/new/', views.fibreoptique_new, name='fibreoptique_new'),
    path('fibres/<int:pk>/edit/', views.fibreoptique_edit, name='fibreoptique_edit'),
    path('fibres/<int:pk>/delete/', views.fibreoptique_delete, name='fibreoptique_delete'),


]