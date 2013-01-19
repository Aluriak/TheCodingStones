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
        self.res_bouton_oui = pygame.image.load(
                "ressources/graphique/boutons/oui_black.bmp")
        self.res_bouton_ouiSel = pygame.image.load(
                "ressources/graphique/boutons/oui_red.bmp")
        self.res_bouton_non = pygame.image.load(
                "ressources/graphique/boutons/non_black.bmp")
        self.res_bouton_nonSel = pygame.image.load(
                "ressources/graphique/boutons/non_red.bmp")
        self.res_menu_back = pygame.image.load(
                "ressources/graphique/menu/menu_background.bmp")
        self.res_menu_title = pygame.image.load(
                "ressources/graphique/menu/menu_title.bmp")
        self.res_menu_userBig = pygame.image.load(
                "ressources/graphique/menu/user_big.bmp")
        self.res_menu_userSmall = pygame.image.load(
                "ressources/graphique/menu/user_small.bmp")


    def afficherJeu(self, ecran, carte, joueur, logs):
        """
        affiche le jeu dans l'écran
        """
        corres = {
            'Terre' : ' ',
            'Mur' : 'X',
            'Eau' : '~',
            'Trou' : 'O',
            'Terre O' : ' '
        }
        for i in map:
            for j in i:
                print(corres[i])
            print('\n')

        pass


    def afficherMenu_under(self, ecran, selection, 
                           carSec, carIhm, carKer, carHar):
        """ 
        sous traitance de la fonction afficherMenu()
        """
        nomChamps = "" # nom du champs à afficher
        # éléments à afficher
        background = self.res_menu_back.get_rect() # background
        titlepos = self.res_menu_title.get_rect() # titre
        titlepos.centerx = ecran.get_width()/2
        titlepos.centery = ecran.get_height()/6

        # intégration du texte
        font = pygame.font.Font(None, 30) # font utilisé
        print selection
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


    def afficherMenu(self, ecran):
        """
        affiche le menu dans l'écran
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
            print selection
            self.afficherMenu_under(ecran, selection, 
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
                    if event.key == pygame.K_DOWN:
                        selection += 1
                        # si on est arrivés en bout de menu, on va en haut
                        if selection == 6:
                            selection = 1
                    if event.key == pygame.K_RIGHT:
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
                    if event.key == pygame.K_LEFT:
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


        # retour
        return {'carSec':carSec,'carIhm':carIhm,'carKer':carKer,'carHar':carHar}


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
S'équiper ?""".format(objet.nom, objet.poids, objet.carac[CARAC_SECU],
                        objet.carac[CARAC_IHM],
                        objet.carac[CARAC_KERNEL],
                        objet.carac[CARAC_HARD]), 
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
        pygame.display.flip()




