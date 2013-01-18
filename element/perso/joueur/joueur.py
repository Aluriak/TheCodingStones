# -*- coding: utf-8 -*-

import settings



#########################
# JOUEUR (CLASS)        #
#########################
class Joueur(Perso):
    """
    Classe du joueur, dérivant de Perso.
    """

    
    def __init__(self, nom, carSec = 10, 
                 carIhm = 10, carKernel = 10, carHard = 10):
        """
        Initialise le joueur, selon Element
        Arguments :
            - nom (string)
            - carac securité (entier, 10 PD)
            - carac ihm (entier, 10 PD)
            - carac kernel (entier, 10 PD)
            - carac hard (entier, 10 PD)
        """
        Perso.__init__(self, nom, carSec, carIhm, carKernel, carHard);

    



