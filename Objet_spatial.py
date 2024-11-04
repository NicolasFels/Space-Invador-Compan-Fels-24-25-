"""
Compan Nolwenn
04/11/2024
But : création des différents objets spatiaux
à faire : tout
fait: rien
"""

class Objet_spatial():
    def __init__(self, nom, depart, forme, vitesse):
        """initialisation des variables"""
        self.nom = nom
        self.position = depart
        self.hit_box = forme
        self.vitesse = vitesse
        self.collision=False
        
    def collision ():
        """toutes les collisions"""
        return
  

class Tir(Objet_spatial):
    """gestion des tirs"""
    
class Ennemis (Objet_spatial):
    """gestion des ennemis"""
    def deplacement(self.position, dx):
        while self.collision==False:
            self.x += dx
        # self.y += dy


class Joueur(Objet_spatial):
    """gestion du joueur"""
