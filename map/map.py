#!/usr/bin/env python

"""
File : map.py

Gestion de la map.
"""

from random import choice, random

class Map:
    """
    Attributs :

        map => map elle même
        longueur => longueur
        largeur => largeur
    """

    types = {
        'Trou' : 2 ,
        'Mur' : 12,
        'Eau' : 4,
        'Terre' : 20,
    }

    def __init__(self, longueur, largeur):
        """
        constructeur
        """

        self.longueur = longueur
        self.largeur = largeur

        # générer la map elle même.
        self.map = [[choice(self.generer_liste_types()) for _ in range(self.largeur)] for __ in range(self.longueur)]

    def generer_liste_types(self):
        """ genere une liste des possibles pour les cases """
        types = []
        for t in Map.types.keys():
            for n in range(Map.types[t]):
                types.append(t)

        return types

	def generer_apparition_monstres(self):
		""" défini l'apparition de monstres (seulement si le joueur n'est pas dans un trou)"""
		if self.types == "Terre":
			if random() < 0.15:
				return random(self.liste_monstres)
		else:
			return "Aucune apparition !"
