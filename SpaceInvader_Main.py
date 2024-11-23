'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Fichier principal du jeu Space Invader, excecute le lancement du jeu;
Fait: Creation d'un visuel et d'un jeu, puis lancement du visuel;
A faire: Voir si c'est plus propre de realiser une fonction main puis de l'appeler;
'''
#Bibliotheques personnelles
from SpaceInvader_ClasseVisuel import Visuel
from SpaceInvader_ClasseJeu import Jeu

#Lancement de la fenetre graphique et du jeu
mv = Visuel()
mg = Jeu(mv)
mv.fMainloop()