# -*- coding: utf-8 -*-

from settings import *



#########################
# JOUEUR (CLASS)        #
#########################
class Joueur(Perso):
    """
    Classe du joueur, dérivant de Perso.
    """

    
    def __init__(self, nom, poidsMax = 10, cafe = 42, carSec = 10, 
                 carIhm = 10, carKernel = 10, carHard = 10):
        """
        Initialise le joueur, selon Element
        Arguments :
            - nom (string)
            - poids maximal portable (entier positif)
            - carac securité (entier, 10 PD)
            - carac ihm (entier, 10 PD)
            - carac kernel (entier, 10 PD)
            - carac hard (entier, 10 PD)
        """
        Perso.__init__(self, nom, poidsMax, cafe, 
                       carSec, carIhm, carKernel, carHard);
        self.poidsEquipement = 0 # pas d'objets équipés, donc poids porté à 0
        self.poidsMax = poidsMax # poids maximum portable
        # le poids max doit toujours être supérieur ou égal 
        #       au poids de l'équipement. (logique, non ?)
        self.x = 0
        self.y = 0



    # fonction de mouvements
    # ce sont de simple accesseurs pas franchement PEP8 friendly,
    # mais elles sont limites plus lisibles comme ça
    def coords(self): return (self.x, self.y)
    def droite(self): self.x += 1
    def gauche(self): self.x -= 1
    def haut(self): self.y += 1
    def bas(self): self.y -= 1


    



