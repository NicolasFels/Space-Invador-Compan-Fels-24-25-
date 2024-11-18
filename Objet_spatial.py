"""
Compan Nolwenn
04/11/2024
But: création de la classes Objet_spatial
        ->initialiser un model pour caracteriser tout les objets (nom, position, vitesse, taille, type)
à faire : reflechir a quoi mettre d'autre
fait: l'idee de base 
"""
#Bibliotheque

#Classe Objet_spatial
class Objet_spatial():
    '''Classe de reference de tous les objets apparaissant a l\'ecran'''
    def __init__(self, nom : str, type : int, position : tuple, taille : tuple, vitesse : tuple):
        '''caractere commun a tous les objets spatiaux.
        nom = le nom de reference de l'entitee; type = -1 pour un ennemi, 0 pour un bloc de protection
         et 1 pour le joueur; positions = refere la position du pixel haut gauche; tailles = refere la
         taille de sa hit box; vitesses = sa vitesse de deplacement en x et en y.
        '''
        self.nom = nom
        self.type = type
        self.position = position
        self.taille = taille
        self.vitesse = vitesse



