# -*- coding: utf-8 -*-

import settings



#########################
# OBJET (CLASS)         #
#########################
class Objet(Element):
    """
    Classe d'objet, dérivant d'Element.
    """


    def __init__(self, nom, poids = 1, carSec = 10,
                 carIhm = 10, carKernel = 10, carHard = 10):
        """
        Initialise l'objet, selon Element
        Arguments :
            - nom (string)
            - poids (entier positif)
            - carac securité (entier, 0 PD)
            - carac ihm (entier, 0 PD)
            - carac kernel (entier, 0 PD)
            - carac hard (entier, 0 PD)
        NOTE : les valeurs envoyées sont des modificateurs, pas des valeurs
        en effet, les personnages équipent des objets dont les caractéristique
              indiquent l'altération de la caractéristique.
        Exemple: équiper un objet ayant 1 en hardware et -2 en securite
              augmente de 1 l'hardware et diminue de 2 la sécurité.
        """
        Element.__init__(self, nom, carSec, carIhm, carKernel, carHard);
        self.poids = poids



