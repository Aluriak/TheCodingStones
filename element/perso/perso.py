# -*- coding: utf-8 -*-

from settings import *
from element.element import Element

#########################
# PERSO  (CLASS)        #
#########################
class Perso(Element):
    """
    Classe de personnage, ennemi ou joueur, dérivant d'Element
    """
    def __init__(self, nom, poidsMax = 100, cafe = 42, carSec = 10, carIhm = 10, carKernel = 10, carHard = 10):
        """
        Initialise le personnage, selon Element
        Arguments :
            - nom (string)
            - poids maximum portable (entier positif)
            - cafe (entier positif)
            - carac securité (entier, 10 PD)
            - carac ihm (entier, 10 PD)
            - carac kernel (entier, 10 PD)
            - carac hard (entier, 10 PD)
        """
        Element.__init__(self, nom, carSec, carIhm, carKernel, carHard)
        self.cafe = cafe # taux de cafe
        self.equipements = [] # liste d'objets
        self.poidsEquipement = 0 # pas d'objets équipés, donc poids porté à 0
        self.poidsMax = poidsMax # poids maximum portable
        # le poids max doit toujours être supérieur ou égal
        #       au poids de l'équipement. (logique, non ?)

    def equiperObjet(self, objetCible):
        """
        Équipe l'objet envoyé et opère les modifs à faire sur les
        valeurs du personnage.
        Retourne False si l'objet ne peut être équipé, True si équipé
        """
        # si le joueur peut porter cet objet
        if self.poidsEquipement + objetCible.poids <= self.poidsMax :
            # modification du poids : on ajoute le poids de l'objet
            self.poidsEquipement += objetCible.poids
            # ajout de l'équipement
            self.equipement.append(objetCible)
            # modifs des caractéristiques
            self.carac[CARAC_SECURITE]      += objetCible.carac[CARAC_SECURITE]
            self.carac[CARAC_IHM]           += objetCible.carac[CARAC_IHM]
            self.carac[CARAC_KERNEL]        += objetCible.carac[CARAC_KERNEL]
            self.carac[CARAC_HARDWARE]      += objetCible.carac[CARAC_HARDWARE]
            return True # objet équipé
        else:
            return False # objet non équipé

    def retirerObjet(self, objetCible):
        """
        Recherche l'objet envoyé en argument dans la liste d'équipement,
        et le supprime, en restaurant les caractéristiques du personnage
        """
        # recherche de l'équipement visé
        # on créé une liste intermédiaire, remplie de tous les objets
        #       qui ne sont pas l'objet cible
        #       si l'on rencontre l'objet visé, on ne l'insère pas dans la liste
        #               et on retire ses caractéristiques au joueur.
        inter = []

        for obj in self.equipements:
            if(obj == objetCible):
                # altération des caracs
                self.carac[CARAC_SECURITE]      -= obj.carac[CARAC_SECURITE]
                self.carac[CARAC_IHM]           -= obj.carac[CARAC_IHM]
                self.carac[CARAC_KERNEL]        -= obj.carac[CARAC_KERNEL]
                self.carac[CARAC_HARDWARE]      -= obj.carac[CARAC_HARDWARE]
                # modification du poids : on retire le poids de l'objet
                self.poidsEquipement -= obj.poids
            else:
                inter.append(obj) # on ajoute l'objet à la liste intermédiaire
        # la liste intemédiaire écrase la liste régulière d'équipement
        self.equipement = inter

    def perte_cafe(self, quantite):
        """ applique les pertes en cafés """
        self.cafe -= quantite

    def vivant(self):
        """ renvoie True si le perso est vivant """
        return (self.cafe > 0)

    def peut_equiper(self, poids_objet):
        """
        retourne True si le poids de l'objet que l'on voudrait équiper + ceux des objets déjà équipés ne dépasse pas
        le poids max acceptable
        """
        return ((self.poidsEquipement+poids_objet) <= self.poidsMax)
