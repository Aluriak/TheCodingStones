# -*- coding: utf8 -*-

import pygame
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

    - ajouterLogs(logs): attent une liste de chaînes. Chaque chaîne sera
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
        format du tuple : ('nom', carSec, carIhm, carKernel, carHard)
        """
        # valeurs par défaut pour le moment
        return {'nom': "jean-michel",
                'secu': 10,
                'ihm': 10,
                'kernel': 10,
                'hardware': 10}


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
        self.graphics.afficherDialogObjet(self.ecran, objet)
        reponse = True
        while not self.termine:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    termine = True
                    self.termine = True
                # pression de touches
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return reponse
                    elif event.key ==pygame.K_RIGHT:
                        reponse = False
                    elif event.key == pygame.K_LEFT:
                        reponse = True
                    elif event.key == pygame.K_ESCAPE:
                        self.termine = True
        return False


    def dialogCombat(self, combat):
        """
        Attends un combat, retourne l'action du joueur dans ce
        combat, (combattre ou fuire, dans un premier temps)
        actions possibles :
            - 'fuite'
            - 'combattre'
        Retourne
        """
        # valeurs par défaut
        return 'combattre'


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


    def ajouterLogs(self, logs):
        """
        Attend une liste de chaînes. Chaque chaîne sera
        ajoutée à la liste de logs de l'IHM.
        """
        # on rajoute les éléments de logs dans les logs de l'IHM
        for log in logs:
            self.logs.append(log)


    def utilisateurQuitte(self):
        """
        Retourne vrai si l'utilisateur quitte le jeu
        """
        return self.termine



