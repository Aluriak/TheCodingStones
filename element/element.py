# -*- coding: utf-8 -*-

from settings import *



#########################
# ELEMENT (CLASS)       #
#########################
class Element():
    """
    classe d'élément de jeu.
    tous les éléments sont dérivés de cette classe
    Elle explicite :
          - un nom (string)
          - les caractéristiques de base (dico "nomCarac"=>valCaracEntier)
    """

    def __init__(self, nom, carSec = 10, 
                 carIhm = 10, carKernel = 10, carHard = 10):
        """
        Initialise l'élément
        Arguments :
            - nom (string)
            - carac securité (entier, 10 PD)
            - carac ihm (entier, 10 PD)
            - carac kernel (entier, 10 PD)
            - carac hard (entier, 10 PD)
        """
        self.nom = nom
        self.carac = {
            CARAC_SECU : carSec,
            CARAC_IHM : carIhm,
            CARAC_KERNEL : carKernel,
            CARAC_HARD : carHard,
        }





