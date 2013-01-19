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
        pass


    def afficherJeu(self, ecran, carte, joueur, logs):
        """
        affiche le jeu dans l'écran
        """
        #ecran.fill(0,0,0) # on vide l'écran
        pygame.display.flip()
        pass


    def afficherMenu(self, ecran):
        """
        affiche le menu dans l'écran
        """
        #ecran.fill(0,0,0) # on vide l'écran
        pygame.display.flip()
        pass

    def afficherDialogObjet(self, ecran, objet, reponse):
        """
        affiche la boite de dialogue pour l'objet envoyé.
        reponseest un booléen, décrivant la réponse mise en avant.
        """
        # background
        background = pygame.Surface(screen.get_size())
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

        # On blit tout
        ecran.blit(background, (0, 0))
        pygame.display.flip()


    def afficherDialogCombat(self, ecran, combat, reponse):
        """
        affiche la boite de dialogue pour le combat envoyé
        """
        pygame.display.flip()




