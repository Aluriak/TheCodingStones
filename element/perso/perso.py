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
                 carIhm = 10, carKernel = 10, carHard = 10):
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
        self.equipements = [] # liste d'objets
        

    def equiperObjet(self, objetCible):
        """
        Équipe l'objet envoyé et opère les modifs à faire sur les 
        valeurs du personnage.
        """
        # ajout de l'équipement
        self.equipement.append(objetCible)
        # modifs des caractéristiques
        self.carac[CARAC_SECURITE]      += objetCible.carac[CARAC_SECURITE]
        self.carac[CARAC_IHM]           += objetCible.carac[CARAC_IHM]
        self.carac[CARAC_KERNEL]        += objetCible.carac[CARAC_KERNEL]
        self.carac[CARAC_HARDWARE]      += objetCible.carac[CARAC_HARDWARE]


    
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
        for obj in self.equipement:
            if(obj == objetCible):
                self.carac[CARAC_SECURITE]      -= obj.carac[CARAC_SECURITE]
                self.carac[CARAC_IHM]           -= obj.carac[CARAC_IHM]
                self.carac[CARAC_KERNEL]        -= obj.carac[CARAC_KERNEL]
                self.carac[CARAC_HARDWARE]      -= obj.carac[CARAC_HARDWARE]
            else:
                inter.append(obj) # on ajoute l'objet à la liste intermédiaire
        # la liste intemédiaire écrase la liste régulière d'équipement
        self.equipement = inter
                



