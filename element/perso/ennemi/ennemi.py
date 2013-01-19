# -*- coding: utf-8 -*-

from settings import *
from perso import Perso

#########################
# ENNEMI (CLASS)        #
#########################
class Ennemi(Perso):
	"""
	Classe de l'ennemi, dérivant de Perso.
	"""

	def __init__(self, nom, poidsMax = 100, carSec = 10,
		   carIhm = 10, carKernel = 10, carHard = 10):
	    """
	    Initialise l'ennemi, selon Element
	    Argument :
		        - nom (string)
                - poids maximal portable (entier positif)
		        - carac securité (entier, 10 PD)
                - carac ihm (entier, 10 PD)
                - carac kernel (entier, 10 PD)
                - carac hard (entier, 10 PD)
        """
        Perso.__init__(self, nom, poidsMax, cafe, carSec, carIhm, carKernel, carHard);
