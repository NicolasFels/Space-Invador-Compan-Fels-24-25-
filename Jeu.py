"""
NIcolas FELS
04/11/2024
But: Faire la classe Jeu du space invaders
A faire: tout
"""
from Visuel import Visuel
from Objet_spatial import Objet_spatial

class Jeu():
    def __init__(self,monvisuel):
        self.creation("test", 5, 100, 100,monvisuel)

    def creation(self,nom, vitesse, x, y,monvisuel):
        #self.objet = Objet_spatial(nom, vitesse, x, y)
        monvisuel.canvas.create_rectangle(x, y, x+10, y+10, fill="white")
        