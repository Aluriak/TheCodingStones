# -*- coding: utf8 -*-

"""
Classe qui gère le jeu per se
"""

from map.map import Map
from element.perso.joueur.joueur import Joueur

class Jeu:
    """
    Classe de jeu
    """

    LONGUEUR = 240
    LARGEUR = 666
    NOM = "Blop"

    def __init__(self):

        # on init. la map
        self.map = Map(Jeu.LONGUEUR, Jeu.LARGEUR)

        # on init le joueur
        self.joueur = Joueur(nom=Jeu.NOM)

       # on se gratte les....


    def start(self):
        """ fonction qui bosse (la seule qui bosse ici en fait....) """

        while 1:
            pass
