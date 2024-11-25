"""
Nicolas FELS
04/11/2024
But: Creation de la classe jeu qui va gerer toutes les actions et reaction en jeu
    ->Fonctions fCreation, fCollision, fDeplacement, fAction_joueur, fGestion_tour
A faire: 
    ->partie tir de fAction_joueur
    ->fGestion_tour
Fait: Rien
"""
#Bibliotheques originelles
from Visuel import mv, score, fScore, fAffichage, fDeplace, fSupprimer
from Classe_Objet_spatial import Objet_spatial

#Bibliotheque classique
from tkinter import Event

#Creation de la classe Jeu
class Jeu():
    '''Gerer les actions, reactions et inter-actions durant une partie'''
    def __init__(self,visuel):
        '''Initialisation du jeu, mise a 0 du score et apparition du joueur et des protections'''
        self.visuel = visuel
        self.score = score
        self.score = fScore(0, 0)
        self.entity = []                        #Utilisation d'une liste, car plus simple pour stocker et acceder a n'importe quelle entitee
        self.fCreation('Joueur', 1, (281, 572), (30, 50), (2, 2))
        self.visuel.bind('<Key>', self.fAction_joueurAction(self.entity))

    def fCreation(self,nom, type, position, taille, vitesse):
        '''Fonction permettant la creation et l'affichage d'une entite.'''
        entity = Objet_spatial(nom, type, position, taille, vitesse)
        self.entity.append(entity)
        fAffichage(entity)

    def fCollision(entity, entity1, entity2):
        '''Gere quand les hit box de 2 entitees se rencontre'''
        if entity1.position[0] <= entity2.position[0] and entity2.position[0] <= entity1.position[0] + entity1.taille[0]:
            entity.remove(entity1, entity2)
            fSupprimer(entity1)
            fSupprimer(entity2)
        elif entity1.position[0] <= entity2.position[0] + entity2.taille[0] and entity2.position[0] + entity2.taille[0] <= entity1.position[0] + entity1.taille[0]:
            entity.remove(entity1, entity2)
            fSupprimer(entity1)
            fSupprimer(entity2)
        elif entity1.position[1] <= entity2.position[1] and entity2.position[1] <= entity1.position[1] + entity1.taille[1]:
            entity.remove(entity1, entity2)
            fSupprimer(entity1)
            fSupprimer(entity2)
        elif entity1.position[1] <= entity2.position[1] + entity2.taille[1] and entity2.position[1] + entity2.taille[1] <= entity1.position[0] + entity1.taille[0]:
            entity.remove(entity1, entity2)
            fSupprimer(entity1)
            fSupprimer(entity2)

    def fDeplacement(Liste_entity, entity, sens : int, direction : int):
        '''Gere le deplacement dans la base de données de l'objet spatial, puis à l'écran.
        regarde en fonction du sens et de la direction si les parametres de l'entitee permettent
        le deplacement dans '''
        entity.position[direction] += sens * entity.vitesse[direction]
        if entity. position[direction] < 0:
            entity. position[direction] = 0
        elif 612 < entity. position[direction]:
            entity. position[direction] = 612
        elif entity.type == 0 and entity.position[direction] in [0, 612]:
            Liste_entity.remove(entity)
            fSupprimer(entity)
        fDeplace(entity)

    def fAction_joueur(self, event, entity):
        '''Active une reponse approprier a la commande du joueur'''
        action = event.keysym
        if action == 'Left':
            self.fDeplacement(entity[0], -1, 0)
        if action == 'Right':
            self.fDeplacement(entity[0], 1, 0)
        if action == 'Down':
            self.fDeplacement(entity[0], -1, 1)
        if action == 'Up':
            self.fDeplacement(entity[0], 1, 1)
        if action == 'space':
            print('piou')

    def fGestion_tour():
        '''Regarde dans un ordre defini les actions qui se sont excutees pendant le tour et reagit
        en consequences'''