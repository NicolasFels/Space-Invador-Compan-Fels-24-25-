"""
Nicolas FELS
Derniere modification: 21/11/2024
But: Creation de la classe jeu qui va gerer toutes les actions et reaction en jeu
    ->fCreation
    ->fCollision
    ->fDeplacement
    ->fAction_joueur
    ->fScore
    ->fGestion_tour
A faire: 
    ->PB SUR AFFICHAGE PERSO AU DEBUT et BIND
    ->finir fAction
    ->tester le bon fonctionnement
    ->gerer le tir
    ->faire fGestionTour
Fait: 
    ->fCreation
    ->fCollision
    ->fDeplacement
    ->fScore
"""

#Bibliotheque
from ClasseObjet_spatial import Objet_spatial
from ClasseVisuel import Visuel

#Classe Jeu
class Jeu():
    '''Gere les actions, inter actions et reaction'''
    def __init__(self, mv):
        
        #Lien entre le jeu et le visuel
        self.visuel = mv

        #Mise a O du score du joueur
        self.Totalpts = 0
        
        #Creation de la liste des entitees
        self.entity = []

        #Creation du joueur
        self.fCreation(1, 3, 0, [300 , 300], (50 , 30), [1 , 0])            #modifier les parametres de tests 

        #Ajout des event
        #self.visuel.fBindKey(self.fAction_joueur(self.entity))

    def fCreation(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Creer une entitee, l'ajoute a la liste des entitees et l'affiche a l'ecran'''
        #Creation de l'entitee
        objet = Objet_spatial(type, vie, valeur, position, hitbox, vitesse)
        #Ajout dans la liste des entitees
        self.entity.append(objet)
        #Affichage dans le visuel
        self.visuel.fAffichage(objet)
            
    def fDeplacement(self, objet, sens, direction):
        '''Gere le deplacement dans la base de données de l'objet spatial, puis à l'écran.
        regarde en fonction du sens et de la direction si les parametres de l'entitee permettent'''
        #Deplacement dans les donnees
        objet.position[direction] += sens * objet.vitesse[direction]
        if objet.position[direction] < 0:
            objet.position[direction] = 0
        elif 612 < objet. position[direction]:
            objet.position[direction] = 612
        elif objet.type == -1 and objet.position[direction] in [0, 612]:
            self.entity.remove(objet)
            self.visuel.fSupprimer(objet)
        #Deplacement sur la fenetre
        self.visuel.fDeplace(objet, sens, direction)

    def fAction_joueur(self, event):
        '''Active une reponse appropriee a la commande du joueur'''
        action = event.keysym
        if action == 'Left':
            self.fDeplacement(self.entity[0], -1, 0)
        if action == 'Right':
            self.fDeplacement(self.entity[0], 1, 0)
        if action == 'Down':
            self.fDeplacement(self.entity[0], -1, 1)
        if action == 'Up':
            self.fDeplacement(self.entity[0], 1, 1)
        if action == 'space':
            print('piou')

    def fCollision(self, objet1, objet2):
        '''Gere quand les hit box de 2 objet se rencontre'''
        collision = False
        if objet1.position[0] <= objet2.position[0] and objet2.position[0] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        elif objet1.position[0] <= objet2.position[0] + objet2.taille[0] and objet2.position[0] + objet2.taille[0] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        elif objet1.position[1] <= objet2.position[1] and objet2.position[1] <= objet1.position[1] + objet1.taille[1]:
            collision = True
        elif objet1.position[1] <= objet2.position[1] + objet2.taille[1] and objet2.position[1] + objet2.taille[1] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        if collision == True:
            self.entity.remove(objet1, objet2)
            self.visuel.fSupprimer(objet1)
            self.visuel.fSupprimer(objet2)
    
    def fScore(self, Newpts : int):
        '''Permet d'afficher en temps reel le score du joueur'''
        self.Totalpts += Newpts
        self.visuel.score.set('Score actuel: ' + str(self.Totalpts))

    def fGestionTour(self):
        pass
