# -*- coding: utf8 -*-

"""
Classe qui gère le jeu per se
"""

from sys import exit
from json import load
from random import randrange, choice
from glob import glob

from map.map import Map
from ihm.ihm import IHM
from combat.combat import Combat
import settings
from element.perso.joueur.joueur import Joueur
from element.perso.ennemi.ennemi import Ennemi
from element.objet.objet import Objet

class Jeu:
    """
    Classe de jeu
    """
    def __init__(self):

        # init IHM
        self.ihm = IHM(hauteur=settings.FENETRE_LONGUEUR, largeur=settings.FENETRE_LARGEUR)
        donnees_joueur = self.ihm.menuDemarrage()
        self.ihm.log(['Données joueurs récupérées'])

        # on init. la map
        self.ihm.log(['Création de la Map'])
        self.map = Map(settings.LONGUEUR, settings.LARGEUR)

        # on init le joueur
        self.ihm.log(['Creation du joueur'])
        self.joueur = Joueur(nom = "Richard",
                             carSec = donnees_joueur['secu'],
                             carIhm = donnees_joueur['ihm'],
                             carKernel = donnees_joueur['kernel'],
                             carHard = donnees_joueur['hardware']
                            )

        # init du jeu (IHM)
        self.ihm.log(['Initialiser jeu'])
        self.ihm.initialiserJeu(self.joueur, self.map)

        self.objets = {}

        # pas pour le prochain monstre
        self.ihm.log(['Tirage au sort du nombre de pas'])
        self.reinit_pas()

        self.ihm.log(['Création de la liste des monstres'])
        self.generer_liste_monstres()

    def stop(self):
        sys.exit

    def start(self):
        """ fonction qui bosse (la seule qui bosse ici en fait....) """

        self.ihm.log(['On attaque la boucle infinie'])

        while 1:

            # 1. afficher le jeu
            self.ihm.afficherJeu()

            if self.ihm.utilisateurQuitte(): self.stop()

            # 2. attendre un mouvement
            # 3. IHM nous file la direction
            mouv = self.ihm.mouvement()

            if self.ihm.utilisateurQuitte(): self.stop()

            # 4. on demande à la map si c'est OK
            # 5. on fait buoger le joueur si OK

            #juste pour faciliter l'accès
            x = self.joueur.x
            y = self.joueur.y
            if mouv == "haut":
                if self.map.case_libre(x, y-1):
                    self.joueur.haut()
                else: continue
            elif mouv == "droite":
                if self.map.case_libre(x+1, y):
                    self.joueur.droite()
                else: continue
            elif mouv == "bas":
                if self.map.case_libre(x, y+1):
                    self.joueur.bas()
                else: continue
            elif mouv == "gauche":
                if self.map.case_libre(x-1, y):
                    self.joueur.gauche()
                else: continue
            else:
                pass # quitter le jeu

            # on retire 1 au compteur de pas
            self.pas_pour_monstre -= 1

            # 6.1. monstre ?
            if not self.pas_pour_monstre:
                self.ihm.log(["C'est l'heure du monstre"])

                # 7.1. on l'instancie
                monstre = self.spawn_monstre()

                # 8.1. on génère un combat
                combat = Combat(self.joueur, monstre)

                # 9.1. on refourgue le combat à l'ihm  qui affiche un dialog
                if self.ihm.utilisateurQuitte(): self.stop()
                choix_combat = self.ihm.dialogCombat(combat)
                if choix_combat == 'combattre':
                    combat.combat()
                else:
                    combat.fuite()

                self.ihm.finCombat(combat)
                if self.ihm.utilisateurQuitte(): self.stop()
                self.reinit_pas()

            # 6.2. objet ?
            # 7.2. on le récupère/on l'instancie
            # 8.2. on le refourgue à l'IHM qui affiche un dialog
            # 9.2. l'user répond et on prend en compte son choix
            self.ihm.log(["Checks pour les objets"])
            if self.ihm.utilisateurQuitte(): self.stop()
            self.objet_trouve()


    def generer_liste_monstres(self):
        """
        génère une liste de monstres à partir des fichiers dans RESSOURCES_PATH/monstres
        """

        self.ihm.log(["Generation de la liste de monstres"])

        # la première liste (celle à l'intérieure récupère la liste des fichiers via glob() et vire le path jusqu'au
        # fichier. La seconde enlève le .json à la fin
        self.liste_monstres =  [__.split('.')[0] for __ in [_.split('/')[-1] for _ in glob('{0}/monstres/*.json'.format(settings.RESSOURCES_PATH))]]


    def objet_trouve(self):
        """ Demande à la map si un objet est là et instancie l'objet au besoin """

        nom_objet = self.map.objet_present(self.joueur.x, self.joueur.y)
        if not nom_objet == "": # s'il y a un objet dans cette case
            if nom_objet in self.objets.keys():
                objet = self.objets[nom_objet]
            else:
                # on instancie l'objet
                donnees_objet = load(open('{0}/objets/{1}.json'.format(settings.RESSOURCES_PATH, nom_objet)))

                objet = Objet(
                    nom_objet,
                    poids = donnees_objet['poids'],
                    carSec = donnees_objet['carSec'],
                    carIhm = donnees_objet['carIhm'],
                    carKernel = donnees_objet['carKernel'],
                    carHard = donnees_objet['carHard']
                )
                self.objets[nom_objet] = objet

            if self.joueur.peut_equiper(objet.poids):
                if self.ihm.dialogObjet(objet): # vrai si l'usr souhaite garder l'objet
                    resultat_equipement = self.joueur.equiperObjet(objet)


    def spawn_monstre(self):
        """ choisit un monstre au hasard, l'instancie et le retourne """
        nom_monstre = choice(self.liste_monstres)

        donnees_monstre = load(open('{0}/monstres/{1}.json'.format(settings.RESSOURCES_PATH, nom_monstre)))

        monstre = Ennemi(
            nom_monstre,
            cafe = donnees_monstre['cafe'],
            carSec = donnees_monstre['carSec'],
            carIhm = donnees_monstre['carIhm'],
            carKernel = donnees_monstre['carKernel'],
            carHard = donnees_monstre['carHard']
        )
        return monstre


    def reinit_pas(self):
        """ Réinitialise le nombre de pas pour le prochain monstre """
        self.pas_pour_monstre = randrange(
            settings.PAS-settings.PAS/2,
            settings.PAS+settings.PAS/2
        )

