# -*- coding: utf-8 -*-

"""
File : map.py

Gestion de la map.
"""

from random import choice, random, randrange
from glob import glob
from re import sub
import os

import settings


class Map:
    """
    Attributs :

        map => map elle même
        longueur => longueur
        largeur => largeur
    """

    # types = {
    #     'Trou' : 2 ,
    #     'Mur' : 12,
    #     'Eau' : 4,
    #     'Terre' : 30,
    # }
    types = {
        'Trou' : 6 ,
        'Mur' : 42,
        'Eau' : 10,
    }

    def __init__(self, longueur, largeur):
        """
        constructeur
        """

        self.longueur = longueur
        self.largeur = largeur
        self.liste_objets = self.generer_liste_objets()

        # générer la map elle même.
        types = self.generer_liste_types()
        self.map = self._generer_map()

    def _generer_map(self):
        # v1
        # return [[choice(types) for _ in range(self.largeur)] for __ in range(self.longueur)]
        # v2
        # on génère une map "blanche" et on la rempli à coup de blocs

        from blocs import blocs

        map = [['Terre' for _ in range(self.largeur)] for __ in range(self.longueur)]
        for i in Map.types.keys():
            bloc = choice(blocs)
            bloc = bloc.splitlines()

            for j in range(Map.types[i]):
                 x = randrange(self.largeur-len(bloc[0]))
                 y = randrange(self.longueur-len(bloc))
                 try:
                     for x_cur in range(len(bloc[0])):
                         for y_cur in range(len(bloc)):
                             if bloc[y_cur][x_cur] != 0:
                                 map[y+y_cur][x+x_cur] = i
                 except IndexError:
                     continue

        return map



    def generer_liste_types(self):
        """ genere une liste des possibles pour les cases """
        types = []
        for t in Map.types.keys():
            for n in range(Map.types[t]):
                types.append(t)

        return types

    def generer_liste_objets(self):
        """
        génère une liste d'objets à partir des fichiers dans RESSOURCES_PATH/objets
        """
        return [__.split('.')[0] for __ in [_.split('/')[-1] for _ in glob('{0}/objets/*.json'.format(settings.RESSOURCES_PATH))]]

    def case_libre(self, x, y):
        """
        répond True si la case est libre
        """
        return (self.map[y][x].split(' ')[0] == "Terre")


    def positionnement_objet(self):
        """ place aléatoirement les objets sur la map """
        for i in map:
            for j in i:
                if self.types == "Terre":
                    if random() <= 0.001:
                        self.types = "Terre O"

    def affichage(self):
        """ affcichage de la map """
        corres = {
            'Terre' : ' ',
            'Mur' : 'X',
            'Eau' : '~',
            'Trou' : 'O',
            'Terre O' : '@'
        }

        for i in self.map:
            print(''.join([corres[_] for _ in i]))


    def objet_present(self, x, y):
        """ retourne le type d'objet si présent """
        if self.map[y][x] == "Terre O":
            return choice(self.liste_objets)
        else:
            return ''
