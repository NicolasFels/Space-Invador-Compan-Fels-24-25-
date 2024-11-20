"""
Compan Nolwenn
Derniere modification: 20/11/2024
But: création de la classes Objet_spatial
        ->initialiser un model pour caracteriser tout les objets (type, vie, valeur, position, hitbox, vitesse)
à faire : reflechir sur la gestion de l'affichage (caracteristique forme)
fait: creation de la classe avec les parametres de base
"""
#Bibliotheque

#Classe Objet_spatial
class Objet_spatial():
    '''Classe de reference de tous les objets apparaissant a l\'ecran'''
    def __init__(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''caracteres communs a tous les objets spatiaux.
        type: -2 ennemi, -1 tir, 0 bloc, 1 joueur
        vie: 1 pour ennemi, tir et bloc; 3 pour joueur
        position: liste contenant la position [x, y]
        hitbox: tuple contenant la taille selon x et y (taillex, tailley)
        vitesse: liste contenant la vitesse de base selon x et y [vitx, vity]
        forme: de base à None, quand l'objet sera creer sera relier a son apparence sur la fenetre
        '''
        self.type = type
        self.vie = vie
        self.valeur = valeur
        self.position = position
        self.hitbox = hitbox
        self.vitesse = vitesse
        self.forme = None                       #Amener a changer selon la façon dont sera gérer l'affichage




