# -*- coding: utf8 -*-
#!/usr/bin/env python

from random import choice

# On définit la taille du lab
h = 31
v = 31

# Définition de la class tableau
class Lab:
	"""
	Attributs :
		- lab => le lab
		- a => valeur d'affichage
		- t => valeur de traitement
	"""

	def __init__(self, h, v):
		"""
		Constructeur
		"""
# Création de liste de liste de taille = largeur x longueur
		self.a = [[' ' for _ in range(h)] for __ in range(v)]
		self.t = [[' ' for _ in range(h)] for __ in range(v)]

# On part du principe qu'il n'existe qu'une seule entrée dans le lab.a
# Le but est d'arriver au milieu afin de faire quelque chose

# 15 = Les 4 murs sont présent
# 1 = Mur gauche
# 2 = Mur haut
# 4 = Mur droit
# 8 = Mur bas
# 0 = Aucun mur présent

# Index Val Mur
#	- 3 = G + H
#	- 5 = G + D
#	- 6 = H + D
# 	- 7 = H + G + D
# 	- 9 = G + B
# 	- 10 = H + B
# 	- 11 = B + G + H
#	- 12 = B + D
#	- 13 = G + B + D
# 	- 14 = H + B + D

lab = Lab(h, v)

# Ensuite, on creuse aleatoirement dans le bloc
for i in range(len(lab.a)):
	for j in range(len(lab.a[i])):
		lab.a[i][j] = choice(range(15))

# Enfin, on génère un chemin unique afin d'obtenir un lab parfait
lab.t[-1][h/2] = 'D' # En bas au milieu de la ligne
"""
lvl :
	 	- 1 = 30 pas
		- 2 = 50 pas
		- 3 = 70 pas
		- 4 = 100 pas
lvl sera reçu en paramètre & déterminera la difficulté du lab
"""
#DEBUG
lvl = 1
#END DEBUG

# On détermine la difficulté
if lvl == 1:
	nb_pas_max = 30
elif lvl == 2:
	nb_pas_max = 50
elif lvl == 3:
	nb_pas_max = 70
else:
	nb_pas_max = 100

# On se place sur le départ && tant que pas val != nb_pas, on continue
coordX = h/2
coordY = 1

val = 0
last = 0 # Contient le choix précédent
nb_pas = 0

#INDEX Déplacement :
# 1 = Haut
# 2 = Gauche
# 3 = Droite
# 4 = Bas

while nb_pas != nb_pas_max:
	val = choice([1,2,3,4])
	# Afin d'éviter les retours en arrière && sortie de lab
	while ((coordX == 0 and val == 2) or # Tant que X == 0 && Val == 2 OU
			(coordX == h-1 and val == 3) or # Tant que X Hauteur - 1 &&
			(coordY == 0 and val == 1) or
			(coordY == v-1 and val == 4) or
			(last == 1 and val == 4) or
			(last == 4 and val == 1) or
			(last == 2 and val == 3) or
			(last == 3 and val == 2)) and lab.t[coordY][coordX] == '#':
		val = choice([1,2,3,4])
	# On marque le chemin
	lab.t[coordY][coordX] = '#'
	#On creuse le chemin si celui ci n'existe pas
	if val == 1 and (lab.a[coordY][coordX] != ([0,2,4,5,8,9,12,13])):
		lab.a[coordY][coordX] = choice([0,2,4,5,8,9,12,13])
	elif val == 2 and (lab.a[coordY][coordX] != ([0,2,4,6,8,10,12,14])):
		lab.a[coordY][coordX] = choice([0,2,4,6,8,10,12,14])
	elif val == 3 and (lab.a[coordY][coordX] != ([0,1,2,3,8,9,10,11])):
		lab.a[coordY][coordX] = choice([0,1,2,3,8,9,10,11])
	elif val == 4 and (lab.a[coordY][coordX] != ([0,1,2,3,4,5,6,7])):
		lab.a[coordY][coordX] = choice([0,1,2,3,4,5,6,7])
	# En fonction de la valeur, on déplace le curseur
	if val == 1:
		coordY -= 1
	elif val == 2:
		coordX -= 1
	elif val == 3:
		coordX += 1
	else:
		coordY += 1
	last = val # On met à jour le dernier déplacement
	nb_pas += 1

# On place la pièce finale
lab.t[coordY][coordX] = 'A'
# Si le joueur arrive d'en dessous
if last == 1:
	lab.a[coordY][coordX] = 7
# Sinon si le joueur vient de la droite
elif last == 2:
	lab.a[coordY][coordX] = 11
# Sinon si le joueur vient de la gauche
elif last == 3:
	lab.a[coordY][coordX] = 14
# Sinon c'est qu'il arrive d'en haut
else:
	lab.a[coordY][coordX] = 13


# On défini l'entrée dans la pièce
lab.t[h/2][(v/2)-1]='A' # Porte d'entrée dans la pièce centrale, côté gauche

# A la fin de la génération, on parcours le tour du lab.a pour le fermer, puis on creuse la piece central de 3*cases
# Ligne du haut
for i in lab.a:
	if not i[0] in [2,3,6,7,10,11,14]:
		i[0] = choice([2,3,6,7,10,11,14])
# Ligne du bas
for i in lab.a:
	if not i[-1] in [8,9,10,11,12,13,14]:
		i[-1] = choice([8,9,10,11,12,13,14])
		print(i[-1])
# Colonne droite
for j in lab.a:
	if not j[-1] in [4,5,6,7,12,13,14]:
		j[-1] = choice([4,5,6,7,12,13,14])
# Colonne gauche
for j in lab.a:
	if not j[0] in [1,2,5,7,9,11,13]:
		j[0] = choice([1,2,5,7,9,11,13])

# DEBUG :

for i in lab.a:
	print(j)
	print("\n")
