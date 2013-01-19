# -*- coding: utf8 -*-

import pygame


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
                "ressources/graphique/menu/menu_userBig.bmp")
        self.res_menu_userSmall = pygame.image.load(
                "ressources/graphique/menu/menu_userSmall.bmp")


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


    def afficherMenu(self, ecran):
        """
        affiche le menu dans l'écran
        """
        ## background
        #background = pygame.Surface(ecran.get_size())
        #background = background.convert()
        #background.fill((0, 0, 0))

        ## affichage du titre

        ## intégration du texte
        #font = pygame.font.Font("Terminus", 36)
        #text = font.render("Nom : ", 1, (255, 255, 255))
        #textpos = text.get_rect()
        #textpos.centerx = background.get_rect().centerx
        #background.blit(text, textpos)

        ## On blitte tout
        #ecran.blit(background, (0, 0))
        #pygame.display.flip()
        nom = raw_input("Nom : ")
        return (nom, 10,10,10,10)


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




