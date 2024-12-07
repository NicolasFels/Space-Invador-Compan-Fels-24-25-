'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 07/12/2024
But: Realiser un classe Jeu permettant de generer et gerer les donnees du jeu;
Fait: Initialisation du jeu;
    methode de creation des entites;
    methode de creation de vagues;
    methode de suppression des entites si plus de vie;
    methode de deplacement;
    methode de mouvement des ennemis et des tirs;
    methode pour gerer les collisions;
    methode pour reset les donnees du jeu;
    methode pour game over;
A faire: Realiser methode de tir pour les ennemis;
    reflechir a differentes ameliorations possibles;
'''
#Bibliotheque standard
from random import randint

#Bibliotheque personnelle
from SpaceInvader_ClasseObjetSpatial import ObjetSpatial

#Creation de la classe
class Jeu():
    '''Permet la creation de l'instance du jeu, ainsi que de definir les methodes necessaires
    au traitement des donnees durant le jeu'''
    def __init__(self):
        '''Initialisation de l'instance du jeu'''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [281, 572], (25, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation des listes des entites autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []
        self.entity = self.ennemisspeciaux + self.ennemis + self.tirs + self.blocs

        #Creation des blocs
        self.fCreationBlocs()

        #Creation de la premiere vague d'ennemis
        self.nombrevague = 1
        self.fCreationVague()

        #Creation des reperes de mouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemidir = 1
        self.ennemisspeciauxdir = 1

        #Creation des etats de fonctionnement
        self.run = False
        self.gameover = False
        self.tirpossible = True

    #Creation des methodes
    #Methodes de gestion des entites
    def fCreation(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Creation d'un objet spatial et ajout a la liste des entites du jeu'''
        #Creation de l'entite
        objet = ObjetSpatial(type, vie, valeur, position, hitbox, vitesse)
        #Ajout dans la liste des entites correspondantes
        self.fActionListe(objet, 'append')
    
    def fSuppression(self, objet):
        '''Supprime l'objet de la liste des entites si sa vie tombe a 0 et ajoute ses points a Totpts'''
        if objet.vie <= 0:                          #Regarde si l'entite a encore des vies
            self.Totpts += objet.valeur             #Si l'entite n'a plus de vie ajoute son score aux points du joueur
            self.fActionListe(objet, 'remove')      #La supprime des listes ou elle apparait
    
    def fCollision(self, objet):
        '''Verifie si la hitbox de l'objet rencontre une autre hitbox, si oui enleve une vie aux deux objets'''
        for entity in self.entity:
            collision = False
            #Regarde si l'objet dont on regarde les collisions est different de l'entite et si leurs hitboxes se chevauchent
            if entity != objet and entity.position[0] <= objet.position[0] and objet.position[0] <= entity.position[0] + entity.hitbox[0]:
                if entity.position[1] <= objet.position[1] and objet.position[1] <= entity.position[1] + entity.hitbox[1]:
                    collision = True
                elif entity.position[1] <= objet.position[1] + objet.hitbox[1] and objet.position[1] + objet.hitbox[1] <= entity.position[1] + entity.hitbox[1]:
                    collision = True
            elif entity != objet and entity.position[0] <= objet.position[0] + objet.hitbox[0] and objet.position[0] + objet.hitbox[0] <= entity.position[0] + entity.hitbox[0]:
                if entity.position[1] <= objet.position[1] and objet.position[1] <= entity.position[1] + entity.hitbox[1]:
                    collision = True
                elif entity.position[1] <= objet.position[1] + objet.hitbox[1] and objet.position[1] + objet.hitbox[1] <= entity.position[1] + entity.hitbox[1]:
                    collision = True
            #En cas de collision enleve une vie aux 2 objets
            if collision == True:
                objet.vie -= 1
                entity.vie -= 1
        

    def fDeplacement(self, objet, direction : int, sens : int):
        '''Modifie la position d'un objet en fonction de sa vitesse, de la direction et du sens souhaites.
        direction : 0 pour les x, 1 pour les y
        sens: -1 pour la gauche ou le haut, 1 pour la droite ou le bas
        '''
        #Deplacement dans les donnees de l'objet
        objet.position[direction] += sens * objet.vitesse[direction]

    def fTrouverRepere(self):
        '''Trouve l'ennemi avec la position en x la plus faible ou la plus grande.
        ennemidir: -1 pour la gauche, 1 pour la droite 
        '''
        if self.ennemidir in [-1, 1]:
            for entity in self.ennemis:
                if self.ennemidir * self.ennemirepere.position[0] <= self.ennemidir * entity.position[0]:
                    self.ennemirepere = entity

    def fCreationVague(self):
        '''Si la liste des ennemis est vide, creer 8 lignes de 6 ennemis a partir des coordonnees (10, 10).
        Chaque ennemi est espace de 30 avec son voisin et chaque ligne de 10.
        '''
        #Cree une vague d'ennemis classiques, leur vie correspond au nombre de vagues ayant etait cree dans ce jeu
        for y in [50, 90, 130, 170, 210, 250, 290, 330]:
            for x in [10, 60, 110, 160, 210, 260, 310, 360, 410]:
                self.fCreation(-2, 1 * self.nombrevague, 100, [x, y], (25, 30), [10, 10])
        #Augmente le nombre de vagues pour la prochaine vague
        self.nombrevague += 1

    def fCreationEnnemiSpecial(self):
        '''Apres un certain temps, regarde si la liste des ennemis speciaux est vide et en cree 1'''
        self.fCreation(-3, 2, 500, [10, 10], (25, 30), (randint(10, 20), 10))
    
    def fCreationBlocs(self):
        '''Creer tous les blocs de protection a des positions precises'''
        #Cree trois zones de protection
        for bloc in [60, 260, 460]:
            for y in [532, 541, 550]:
                for x in [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]:
                    self.fCreation(0, 1, 0, [bloc + x, y], (8, 8), [0, 0])

    #Methode de fonctionnement
    def fReset(self):
        '''Remet tous les parametres du jeu a leur valeur d'origine '''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [281, 572], (25, 30), [5, 0])   #Valeurs de tests amenees a changer
        
        #Creation des listes des entites autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []
        self.entity = self.ennemisspeciaux + self.ennemis + self.tirs + self.blocs

        #Creation des blocs
        self.fCreationBlocs()

        #Creation de la premiere vague d'ennemis
        self.nombrevague = 1
        self.fCreationVague()

        #Creation des reperes de mmouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemidir = 1
        self.ennemisspeciauxdir = 1

        #Creation des etats de fonctionnement
        self.run = False
        self.gameover = False
        self.tirpossible = True
    
    def fActionListe(self, objet, action):
        '''Permet en fonction de l'action choisie ('remove' ou 'append') d'ajouter ou
        d'enlever l'objet a la liste correspondante a son type'''
        cible = self.ennemis
        #Test le type de l'entite pour savoir ou agir
        if objet.type == 0:
            cible = self.blocs
        elif objet.type == -1:
            cible = self.tirs
        elif objet.type == -2:
            cible = self.ennemis
        elif objet.type == -3:
            cible = self.ennemisspeciaux
        #Regarde quel action est demandee et l'effectue dans la liste correspondante au type de l'entite et dans celle de toutes les entites
        if action == 'remove':
            cible.remove(objet)
            self.entity.remove(objet)
        elif action == 'append':
            cible.append(objet)
            self.entity.append(objet)

    def fGameOver(self):
        '''Verifie si le joueur a encore des vies ou non, s'il n'en a plus
        change la valeur de gameover en True'''
        if self.joueur.vie <= 0:
            self.gameover = True
            self.run = False
            print('GAME OVER')

    def fTirPossible(self):
        '''Active ou desactive la possibilite de tir'''
        if self.tirpossible == True:
            self.tirpossible = False
        else:
            self.tirpossible = True