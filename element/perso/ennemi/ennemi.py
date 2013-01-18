# -*- coding: utf-8 -*-

import settings



#########################
# ENNEMI (CLASS)        #
#########################
class Ennemi(Perso):
	"""
	Classe de l'ennemi, dérivant de Perso.
	"""

	def __init__(self, nom, carSec = 10,
		   carIhm = 10, carKernel = 10, carHard = 10):
	"""
	Initialise l'ennemi, selon Element 
	Argument :
		- nom (string)
		- carac securité (entier, 10 PD)
                - carac ihm (entier, 10 PD)
                - carac kernel (entier, 10 PD)
                - carac hard (entier, 10 PD)
        """
	Perso.__init__(self, nom, carSec, carIhm, carKernel, carHard);
	


	


