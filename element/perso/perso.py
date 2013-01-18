# -*- coding: utf-8 -*-

import settings



#########################
# PERSO  (CLASS)        #
#########################
class Perso(Element):
    """
    Classe de personnage, ennemi ou joueur, dérivant d'Element
    """
    
    def __init__(self, nom, cafe = 100, carSec = 10, 
                 carIhm = 10, carKernel = 10, carHard = 10, equipement = []):
        """
        Initialise le personnage, selon Element
        Arguments :
            - nom (string)
            - carac securité (entier, 10 PD)
            - carac ihm (entier, 10 PD)
            - carac kernel (entier, 10 PD)
            - carac hard (entier, 10 PD)
        """
        Element.__init__(self, nom, carSec, carIhm, carKernel, carHard);
        self.cafe = cafe # taux de cafe
        

    



