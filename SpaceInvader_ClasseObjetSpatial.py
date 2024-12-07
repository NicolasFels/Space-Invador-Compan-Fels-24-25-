'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Realiser une classe regroupant les caracteristiques et methodes standards de tous les differents objets spatiaux;
Fait: Initialisation des objets avec tous les parametres utiles;
A faire: Reflechir a differentes ameliorations possibles;
'''
#Bibliotheque standard
from tkinter import PhotoImage

#Creation de la classe ObjetSpatial
class ObjetSpatial():
    '''Regroupe les caracteristiques et methodes communes a tous les objets spatiaux'''
    def __init__(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Initialisation des caracteristiques communes a tous les objets spatiaux.
        type: -3 ennemi special, -2 ennemi, -1 tir, 0 bloc neutre, 1 joueur
        vie: le nombre de tirs ou contatcs necessaires a detruire l'objet
        valeur: les points a ajouter au score quand l'objet est detruit
        position: une liste de la position du pixel haut gauche de l'objet [x, y]
        hitbox: un tuple contenant la taille de la hit box de l'objet selon les coordonnees (x, y)
        vitesse: une liste contenant la vitesse de deplacement de l'objet
        '''
        self.type = type
        self.vie = vie
        self.valeur = valeur
        self.position = position
        self.hitbox = hitbox
        self.vitesse = vitesse
        self.id = 0