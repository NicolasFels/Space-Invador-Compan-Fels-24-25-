"""
Nicolas FELS
04/11/2024
But: Main du jeu space invaders
A faire:
"""
import tkinter as tk

from Visuel import Visuel
from Jeu import Jeu
from Objet_spatial import Joueur

# test = Objet_spatial("bob", 5, 100, 100)
# test.creation(test.x, test.y)
# test=Joueur("bob,",1,100,100)
# test.deplacement_joueur()

# for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
#     Visuel.bind(key, test.deplacement_joueur)

mv = Visuel()
mg = Jeu(mv)

mv.mf.mainloop()