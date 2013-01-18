# -*- coding: utf8 -*-



#########################
# IHM  (CLASS)          #
#########################
class ihm():
    """
    Travaille avec une map, renvois les actions utilisateur.
    Reçois les logs du jeu, pour les accumuler et permettre leur affichage.
    Reçois aussi les combats pour les afficher, ou les objets, pour demander
    à l'utilisateur s'il en veut ou pas.
    """
    import pygame

    def __init__(self):
        """
        Démarre pygame.
        Charge les ressources.
        Gère un menu où l'utilisateur peut entrer :
            - nom
            - caracs
        Renvois le joueurs avec les caracs et le nom choisis.
        """
        # initialisation de pygame
        pygame.display.init()
        # retour du joueur
        return Joueur("Jean-michel")


    def actualiserJeu(carteJeu):
        """
        Attend une carte du jeu, qui écrasera la fonction précédente.
        """

    def affichage(self):
        """
        Affiche le jeu selon les attributs de la classe.
        Si un objet ou un combat, lance


