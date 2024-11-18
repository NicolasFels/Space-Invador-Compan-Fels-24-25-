"""
Nicolas FELS
04/11/2024
But: Creation de la classe jeu qui va gerer toutes les actions et reaction en jeu
    ->Fonctions
A faire: 
    ->
Fait: Rien
"""
#Bibliotheques
from Visuel import mv, score, fScore, fAffichage, fDeplacement, fSupprimer
from Classe_Objet_spatial import Objet_spatial

#Creation de la classe Jeu
class Jeu():
    '''Gerer les actions, reactions et inter-actions durant une partie'''
    def __init__(self,visuel):
        '''Initialisation du jeu, mise a 0 du score et apparition du joueur et des protections'''
        self.score = score
        self.score = fScore(0, 0)
        self.entity = []                        #Utilisation d'une liste, car plus simple pour stocker et acceder a n'importe quelle entitee
        self.fCreation('Joueur', 1, (592, 281), (10, 50), (2, 2), visuel)

    def fCreation(self,nom, type, position, taille, vitesse, visuel):
        '''Fonction permettant la creation et l'affichage d'une entite.'''
        entity = Objet_spatial(nom, type, position, taille, vitesse)
        self.entity.append(entity)
        fAffichage(entity, visuel)

    def fCollision():
        '''Gere quand les hit box de 2 entitees se rencontre'''

    def fTir():
        '''Genere un tir du joueur comme d'un ennemi'''
    
    def fAction_joueur():
        '''Active une reponse approprier a la commande du joueur'''

    def fGestion_tour():
        '''Regarde dans un ordre defini les actions qui se sont excutees pendant le tour et reagit
        en consequences'''