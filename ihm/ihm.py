# -*- coding: utf8 -*-



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

**Méthodes d'accès :**
    - __init__(): créé l'IHM. Charge les ressource et pygame.

    - menuDemarrage(): retourne un tuple contenant les données permettant 
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


le joueur et la carte sont les mêmes que ceux manipulés par le jeu. 
Donc, pas besoin de les actualiser.
L'IHM ne modifie jamais les valeurs envoyées, la carte ou le joueur.
    """
    import pygame

    def __init__(self):
        """
        Démarre pygame.
        Charge les ressources.
        """
        # initialisation de pygame
        pygame.display.init() # module graphique
        # autre attributs
        self.logs = ["IHM initialisée"]
        self.joueur = 0 # pas de joueur au départ
        self.carte = 0 # pas de carte au départ


    def menuDemarrage(self): 
        """ 
        Gère un menu où l'utilisateur peut entrer :
            - nom
            - caracs
        Renvois un tuple indiquant ces données. (le jeu pourra alors créer
            un joueur ayant ces carac et ce nom)
        format du tuple : ('nom', carSec, carIhm, carKernel, carHard)
        """
        # valeurs par défaut pour le moment
        return ("jean-michel", 10, 10, 10, 10) 
    

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
        """
        pass


    def mouvement(self): 
        """
        demande un mouvement à l'utilisateur, renvois 'haut', 'bas',
        'gauche' ou 'droite'.
        """
        # valeur par défaut : aléatoire
        return random.choice(['haut', 'bas', 'gauche', 'droite'])


    def dialogObjet(self, objet): 
        """ 
        Attends un objet, retourne vrai si l'utilisateur 
        veux s'en équiper
        """
        # valeurs par défaut
        return True 


    def dialogCombat(self, combat): 
        """ 
        Attends un combat, retourne l'action du joueur dans ce
        combat, (combattre ou fuire, dans un premier temps)
        actions possibles :
            - 'fuite'
            - 'combattre'
        """
        # valeurs par défaut
        return 'combattre'


    def finCombat(combat): 
        """ 
        Attends le combat, considéré terminé. Affiche un écran de 
        fin de combat, et se termine sans rien renvoyer quand l'utilisateur
        quitte l'écran de fin de combat.
        """
        pass


    def gameOver(): 
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




