"""
Compan Nolwenn
04/11/2024
But : création des différents objets spatiaux
à faire : tout
fait: rien
"""
#Bibliotheque
from tkinter import Event, Canvas
#Classes
class Objet_spatial():
    def __init__(self, nom, vitesse,x,y):
        """initialisation des variables"""
        self.nom = nom
        self.vitesse = vitesse
        self.collision=False
        self.x=x
        self.y=y

    def creation (x, y):
        Canvas.create_rectangle(x,y, x+10, y+10, fill='white')


    def collision ():
        """toutes les collisions"""

        return
  

class Tir(Objet_spatial) :
    """gestion des tirs"""
    pass
class Ennemis(Objet_spatial) :
    """gestion des ennemis"""
    def deplacement_ennemis(position, dx) :
        while Objet_spatial.collision==False:
            Objet_spatial.x += dx
        # self.y += dy


class Joueur(Objet_spatial):
    """gestion du joueur"""
    def deplacement_joueur(event):
        gauche=event
