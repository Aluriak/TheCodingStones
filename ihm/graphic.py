# -*- coding: utf8 -*-

import pygame
import time


#########################
# GRAPHIC  (CLASS)      #
#########################
class Graphic:
    """
    Classe graphique.
        Charge les ressources.
    Propose un certain nombre de méthodes, en attendant chaque fois
    l'écran où afficher.
        - afficherJeu(ecran, carte, joueur, logs)
        - afficherMenu(ecran)
        - afficherDialogObjet(ecran, objet, reponse)
        - afficherDialogCombat(ecran, combat)
    """

    # intialisation
    def __init__(self):
        # chargement des ressources
        self.res_menu_back = pygame.image.load(
                "ressources/graphique/menu/menu_background.bmp")
        self.res_menu_title = pygame.image.load(
                "ressources/graphique/menu/menu_title.bmp")


    def afficherJeu(self, ecran, carte, joueur, logs):
        """
        affiche le jeu dans l'écran
        """
        carte.affichage()


    def afficherMenu(self, ecran, selection, 
                           carSec, carIhm, carKer, carHar):
        """ 
        Affiche le menu
        """
        nomChamps = "" # nom du champs à afficher
        # éléments à afficher
        background = self.res_menu_back.get_rect() # background
        titlepos = self.res_menu_title.get_rect() # titre
        titlepos.centerx = ecran.get_width()/2
        titlepos.centery = ecran.get_height()/6

        # intégration du texte
        font = pygame.font.Font(None, 30) # font utilisé
        if selection == 1:
            nomChamps = "SECURITE : "
        else:
            nomChamps = "Securite : "
        nomChamps += str(carSec)
        text1 = font.render(nomChamps, 1, (255, 225, 225)) 
        text1pos = text1.get_rect()
        text1pos.centerx = 80
        text1pos.centery = background.centery - 80
        if selection == 2:
            nomChamps = "IHM : "
        else:
            nomChamps = "Ihm : "
        nomChamps += str(carIhm)
        text2 = font.render(nomChamps, 1, (255, 225, 225)) 
        text2pos = text2.get_rect()
        text2pos.centerx = 80
        text2pos.centery = background.centery - 20
        if selection == 3:
            nomChamps = "KERNEL : "
        else:
            nomChamps = "Kernel : "
        nomChamps += str(carKer)
        text3 = font.render(nomChamps, 1, (255, 225, 225)) 
        text3pos = text3.get_rect()
        text3pos.centerx = 80
        text3pos.centery = background.centery + 40
        if selection == 4:
            nomChamps = "HARDWARE : "
        else:
            nomChamps = "Hardware : "
        nomChamps += str(carHar)
        text4 = font.render(nomChamps, 1, (255, 225, 225)) 
        text4pos = text4.get_rect()
        text4pos.centerx = 80
        text4pos.centery = background.centery + 120
        if selection == 5:
            nomChamps = "GOOOOOO !!!!"
        else:
            nomChamps = "go ?"
        text5 = font.render(nomChamps, 1, (255, 225, 225)) 
        text5pos = text5.get_rect()
        text5pos.centerx = ecran.get_width()/2
        text5pos.centery = background.centery + 180


        # blit des éléments
        ecran.blit(self.res_menu_back, (0, 0))
        ecran.blit(self.res_menu_title, titlepos)
        ecran.blit(text1, text1pos)
        ecran.blit(text2, text2pos)
        ecran.blit(text3, text3pos)
        ecran.blit(text4, text4pos)
        ecran.blit(text5, text5pos)

        # actualisation
        pygame.display.flip()



    def afficherDialogObjet(self, ecran, objet, reponse):
        """
        affiche la boite de dialogue pour l'objet envoyé.
        reponse est un booléen, décrivant la réponse mise en avant.
        """
        # background
        background = pygame.Surface(ecran.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # intégration du texte
        font = pygame.font.Font("Terminus", 36)
        text = font.render("""Objet : {0} 
Poids : {1}
Sécurité : {2}
IHM : {3}
Kernel : {4}
Hardware : {5}
S'équiper ?
{6}""".format(objet.nom, objet.poids, objet.carac[CARAC_SECU],
                        objet.carac[CARAC_IHM],
                        objet.carac[CARAC_KERNEL],
                        objet.carac[CARAC_HARD],
                        reponse), 
                           1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)

        # On blitte tout
        ecran.blit(background, (0, 0))
        pygame.display.flip()


    def afficherDialogCombat(self, ecran, combat, reponse):
        """
        affiche la boite de dialogue pour le combat envoyé
        """
        pass




