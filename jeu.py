# -*- coding: utf8 -*-

"""
Classe qui gère le jeu per se
"""

from json import loads

from map.map import Map
import settings
from element.perso.joueur.joueur import Joueur

class Jeu:
    """
    Classe de jeu
    """

    LONGUEUR = 240
    LARGEUR = 666
    NOM = "Blop"

    def __init__(self):

        # on init. la map
        self.map = Map(Jeu.LONGUEUR, Jeu.LARGEUR)

        # on init le joueur
        self.joueur = Joueur(nom=Jeu.NOM)
        self.objets = {}

    def start(self):
        """ fonction qui bosse (la seule qui bosse ici en fait....) """

        while 1:
            pass

            # 1. afficher le jeu
            # 2. attendre un mouvement
            # 3. IHM nous file la direction
            # 4. on demande à la map si c'est OK
            # 5. on fait buoger le joueur si OK
            # 6.1. objet ?
            # 7.1. on le récupère/on l'instancie
            # 8.1. on le refourgue à l'IHM qui affiche un dialog
            # 9.1. l'user répond et on prend en compte son choix
            # 6.2. monstre ?
            # 7.2. on l'instancie
            # 8.2. on génère un combat
            # 9.2. on refourgue le combat à l'ihm  qui affiche un dialog
            # 10.2.1. on combat => la classe gère le combat
            # 10.2.2. on fuit => on teste la fuite et on voit
            # 11. on renvoie le resultat à l'IHM qui l'affiche
            # retour au 1


    def objet_trouve(self):
        """ Demande à la map si un objet est là et instancie l'objet au besoin """

        nom_objet = self.map.objet_present(self.joueur.x, self.joueur.y)
        if not nom_objet == "": # s'il y a un objet dans cette case
            if objet_nom in self.objets.keys():
                pass # On utilise l'objet de la liste
            else:
                # on instancie l'objet
                file  = open('{0}/objets/{1}.json'.format(settings.RESSOURCES_PATH, nom_objet))
                donnees_objet = loads(file.read())

                objet = Objet(
                    nom_objet,
                    poids = donnees_objet['poids'],
                    carSec = donnees_objet['carSec'],
                    carIhm = donnees_objet['carIhm'],
                    carKernel = donnees_objet['carKernel'],
                    carHard = donnees_objet['carHard']
                )

                resultat_equipement = self.joueur.equiperObjet(objet)
                self.objets[nom_objet] = objet


