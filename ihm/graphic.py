# -*- coding: utf8 -*-



#########################
# GRAPHIC  (CLASS)      #
#########################
class Graphic:
    """
    Classe graphique.
        Charge les ressources.
    Propose un certain nombre de méthodes, en attendant chaque fois
    l'écran où afficher.
        - afficherJeu(ecran, carte, joueur, logs)
        - afficherMenu(ecran)
        - afficherDialogObjet(ecran, objet, reponse)
        - afficherDialogCombat(ecran, combat)
    """
    import pygame

    # intialisation
    def __init__(self):
        # chargement des ressources
        pass


    def afficherJeu(self, ecran, carte, joueur, logs):
        """
        affiche le jeu dans l'écran
        """
        ecran.fill(0,0,0) # on vide l'écran


    def afficherMenu(self, ecran):
        """
        affiche le menu dans l'écran
        """
        ecran.fill(0,0,0) # on vide l'écran

    def afficherDialogObjet(self, ecran, objet, reponse):
        """
        affiche la boite de dialogue pour l'objet envoyé.
        reponseest un booléen, décrivant la réponse mise en avant.
        """
        ecran.fill(0,0,0) # on vide l'écran


    def afficherDialogCombat(self, ecran, combat):
        """
        affiche la boite de dialogue pour le combat envoyé
        """
        ecran.fill(0,0,0) # on vide l'écran




