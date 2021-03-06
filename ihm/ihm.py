# -*- coding: utf8 -*-

import pygame
import time
from graphic import Graphic


#########################
# IHM  (CLASS)          #
#########################
class IHM():
    """
# DOC IHM
Ce document retrace les méthodes d'accès de l'IHM.
Intérêt : savoir comment faire pour interagir, et permettre au developpeur
d'avoir les idées claires (ce qui est très important à trois heures du mat')


## principe
l'IHM fonctionne selon un principe simple :
Elle fait ce que vous lui demandez.
D'abord, créez là, ça paraît logique.
Ensuite, appelez menuDemarrage(), histoire de savoir quel personnage veux le
    joueur. Elle vous renverras ce que le joueur veut pour personnage, sous la
    forme d'un tuple : ('nom', carSec, carIhm, carKernel, carHard)
Ensuite, appelez initialiserJeu(), avec le joueur et la carte en arguments.
    L'IHM se souviendra alors de ces références qu'elle gardera pour afficher
    le jeu avec les données toujours actualisées.

Enfin, dites lui ce que vous voulez : vous pouvez lui faire afficher le jeu,
    lui faire afficher une boite de dialog pour savoir si le joueur veut l'objet
    que vous lui envoyez en argument,...
L'IHM vous renverra des actions correspondant à la volonté de l'utilisateur.

A FAIRE: tester utilisateurQuitte() le plus souvent possible, car il renvois vrai
    quand l'utilisateur veut quitter. Il faudra alors tout arrêter.

**Méthodes d'accès :**
    - __init__(): créé l'IHM. Charge les ressource et pygame.

    - menuDemarrage(): retourne un dico contenant les données permettant
        d'initialiser un joueur;

    - initialiserJeu(joueur, carte): prend les ref vers la carte et le joueur;

    - afficherJeu(): affiche le jeu selon les valeurs connues

    - mouvement(): demande un mouvement à l'utilisateur, renvois 'haut', 'bas',
        'gauche' ou 'droite'.

    - dialogObjet(): attends un objet, retourne vrai si l'utilisateur
        veux s'en équiper

    - dialogCombat(): attends un combat, retourne l'action du joueur dans ce
        combat, (combattre ou fuire, dans un premier temps)

    - finCombat(): attends le combat, considéré terminé. Affiche un écran de
        fin de combat, et se termine sans rien renvoyer quand l'utilisateur
        quitte l'écran de fin de combat.

    - gameOver(): affiche l'écran de fin de jeu, s'arrête quand l'utilisateur
        quitte l'écran de fin de jeu, en ne renvoyant rien.

    - logs(logs): attent une liste de chaînes. Chaque chaîne sera
        ajoutée à la liste de logs de l'IHM.

    - utilisateurQuitte(): retourne vrai si l'utilisateur veut quitter


le joueur et la carte sont les mêmes que ceux manipulés par le jeu.
Donc, pas besoin de les actualiser.
L'IHM ne modifie jamais les valeurs envoyées, la carte ou le joueur.
    """


    def __init__(self, largeur = 600, hauteur = 400):
        """
        Initialisation de pygame.
        Intialisation de Graphic.
        hauteur et largeur de la fenêtre attendue en paramètres.
        """
        # initialisation de pygame
        pygame.display.init() # module graphique
        pygame.font.init() # module de texte
        # Création de l'écran
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        # création du graphic, simplifiant les affichages
        self.graphics = Graphic()
        # autre attributs
        self.logs = ["IHM initialisée"]
        self.joueur = 0 # pas de joueur au départ
        self.carte = 0 # pas de carte au départ
        self.termine = False # vrai si jeu terminé


    def menuDemarrage(self):
        """
        Gère un menu où l'utilisateur peut entrer :
            - nom
            - caracs
        Renvois un dico indiquant ces données. (le jeu pourra alors créer
            un joueur ayant ces carac et ce nom)
            format du dico : {'carSec':int, 'carIhm':int, 'carKer':int, 
                'carHar':int}
        """
        # event 
        termine = False
        carSec = 10
        carIhm = 10
        carKer = 10
        carHar = 10
        selection = 1
        reservePoint = 6
        while not termine:
            # AFFICHAGES
            self.graphics.afficherMenu(self.ecran, selection, 
                                    carSec, carIhm, carKer, carHar)
            # ÉVÈNEMENTS
            for event in pygame.event.get():
                time.sleep(0.1)
                if event.type == pygame.QUIT: 
                    termine = True
                    self.termine = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        termine = True
                        self.termine = True
                    elif event.key == pygame.K_UP:
                        selection -= 1
                        # si on est arrivés en bout de menu, on va en bas
                        if selection == 0:
                            selection = 5
                    elif event.key == pygame.K_DOWN:
                        selection += 1
                        # si on est arrivés en bout de menu, on va en haut
                        if selection == 6:
                            selection = 1
                    elif event.key == pygame.K_RIGHT:
                        if selection == 1 and reservePoint > 0:
                            carSec += 1
                            reservePoint -= 1
                        elif selection == 2 and reservePoint > 0:
                            carIhm += 1
                            reservePoint -= 1
                        elif selection == 3 and reservePoint > 0:
                            carKer += 1
                            reservePoint -= 1
                        elif selection == 4 and reservePoint > 0:
                            carHar += 1
                            reservePoint -= 1
                        elif selection == 5:
                            termine = True
                    elif event.key == pygame.K_LEFT:
                        if selection == 1 and reservePoint <= 6:
                            carSec -= 1
                            reservePoint += 1
                        elif selection == 2 and reservePoint <= 6:
                            carIhm -= 1
                            reservePoint += 1
                        elif selection == 3 and reservePoint <= 6:
                            carKer -= 1
                            reservePoint += 1
                        elif selection == 4 and reservePoint <= 6:
                            carHar -= 1
                            reservePoint += 1
                    elif event.key == pygame.K_RETURN and selection == 5:
                        termine = True


        # retour
        return {'secu':carSec,'ihm':carIhm,'kernel':carKer,'hardware':carHar}


    def initialiserJeu(self, joueur, carte):
        """
        Prend les ref vers la carte et le joueur.
        Oui, c'est tout. Mais si vous oubliez de l'appeler, l'IHM va merder sec.
        """
        self.joueur = joueur
        self.carte = carte


    def afficherJeu(self):
        """
        Affiche le jeu selon les valeurs connues (joueur et carte)
        Retourne faux si l'utilisateur veut quitter
        """
        # appel à graphic pour le jeu
        self.graphics.afficherJeu(self.ecran, self.carte, self.joueur, self.logs)
        pygame.display.flip()
        return not self.termine # retour de l'état du jeu (faux pour quitter)


    def mouvement(self):
        """
        demande un mouvement à l'utilisateur, renvois 'haut', 'bas',
        'gauche' ou 'droite'. Ou False si l'utilisateur veut quitter.
        """
        # affichage du jeu
        self.afficherJeu()
        # boucle event
        while not self.termine:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.termine = True
                # pression de touches
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        return 'haut'
                    elif event.key == pygame.K_DOWN:
                        return 'bas'
                    elif event.key == pygame.K_RIGHT:
                        return 'droite'
                    elif event.key == pygame.K_LEFT:
                        return 'gauche'
                    elif event.key == pygame.K_ESCAPE:
                        self.termine = True
        return False


    def dialogObjet(self, objet):
        """
        Attends un objet, retourne
            True si l'utilisateur veux s'en équiper
            False si il ne veux pas
        """
        reponse = 'oui'
        while not self.termine:
            self.graphics.afficherDialogObjet(self.ecran, objet, reponse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    termine = True
                    self.termine = True
                # pression de touches
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return reponse
                    elif event.key ==pygame.K_RIGHT:
                        reponse = 'non'
                    elif event.key == pygame.K_LEFT:
                        reponse = 'oui'
                    elif event.key == pygame.K_ESCAPE:
                        self.termine = True
        return False


    def dialogCombat(self, combat):
        """
        Attends un combat, retourne l'action du joueur dans ce
        combat, (combattre ou fuire, dans un premier temps)
        actions possibles :
            - 'fuite'
            - 'combat'
        """
        # valeurs par défaut
        reponse = 'fuite'
        while not self.termine:
            self.graphics.afficherDialogCombat(self.ecran, combat, reponse)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.termine = True
                # pression de touches
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return reponse
                    elif event.key ==pygame.K_RIGHT:
                        reponse = 'fuite'
                    elif event.key == pygame.K_LEFT:
                        reponse = 'combat'
                    elif event.key == pygame.K_ESCAPE:
                        self.termine = True
                        reponse = 'fuite'
        return reponse


    def finCombat(self, combat):
        """
        Attends le combat, considéré terminé. Affiche un écran de
        fin de combat, et se termine sans rien renvoyer quand l'utilisateur
        quitte l'écran de fin de combat.
        """
        pass


    def gameOver(self):
        """
        Affiche l'écran de fin de jeu, s'arrête quand l'utilisateur
        quitte l'écran de fin de jeu, en ne renvoyant rien.
        """
        pass


    def log(self, logs):
        """
        Attend une liste de chaînes. Chaque chaîne sera
        ajoutée à la liste de logs de l'IHM, et affichée dans la sortie standard.
        """
        # on rajoute les éléments de logs dans les logs de l'IHM
        for log in logs:
            self.logs.append(log) # ajout dans les logs
            print log # affichage dans la sortie standard


    def utilisateurQuitte(self):
        """
        Retourne vrai si l'utilisateur quitte le jeu
        """
        return self.termine



