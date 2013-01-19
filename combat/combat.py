# -*- coding: utf8 -*-

"""

module gèrant les combats and co

"""

from settings import *


class Combat:
    """

    Classe gérant les combats

    Reçoit en entrée un joueur et un ennemi.

    """

    caracs = [
        CARAC_SECURITE,
        CARAC_IHM,
        CARAC_KERNEL,
        CARAC_HARDWARE
    ]

    def __init__(self, joueur, ennemi):

        self.joueur = joueur
        self.ennemi = ennemi
        self.fin = False
        self.gagnant = "" # vide, joueur ou ennemi ou fuite
        self.perte_totale = 0

    def combat(self):
        """ Fonction gèrant tout le combat en solo, sans action de l'utilisateur """

        # on continue à se taper dessus jusqu'a ce que mort s'en suive
        while not self.fin:

            # on teste chaque caractéristique
            for car in Combat.caracs:
                perte = self.joueur.carac[car] - self.ennemi.carac[car]

                if perte < 0:
                    self.perte_totale -= perte # on ajoute abs(perte) en fait, perte étant négatif
                    self.joueur.perte_cafe(-perte)
                else:
                    self.ennemi.perte_cafe(perte)

                # on teste pour la fin du combat
                self._conditions_fin()
                if self.fin: break


    def fuite(self):
        """ Fonction générant une tentative de fuite """
        somme_carac_joueur = sum([self.joueur.carac[_] for _ in Combat.caracs])
        somme_carac_ennemi = sum([self.ennemi.carac[_] for _ in Combat.caracs])

        diff = somme_carac_joueur - somme_carac_ennemi
        if diff < 0: diff = -diff

        self.joueur.perte_cafe(diff)
        self.fin = True
        self.gagnant = "fuite" # lââââââche !


    def _conditions_fin(self):
        """ change la valeur de self.fin pour donner l'issue du combat """
        if self.joueur.vivant() and not self.ennemi.vivant():
            self.gagnant = "joueur"
        elif self.ennemi.vivant() and not self.joueur.vivant():
            self.gagnant = "ennemi"
        self.fin = True
