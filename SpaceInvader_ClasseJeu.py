'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 25/11/2024
But: Realiser un classe Jeu permettant de generer et gerer les donnees du jeu;
Fait: Initialisation du jeu;
    methode de creation des entitees;
    methode de creation de vague;
    methode de suppression des entitees si plus de vie;
    methode de deplacement;
    methode de mouvement des ennemis et des tirs;
    methode pour gerer les collisions;
    methode pour reset les donnees du jeu;
    methode pour game over;
A faire: Realiser methode de tir pour les ennemis;
    reflechir a differentes ameliorations possibles;
'''
#Bibliotheque personnelle
from SpaceInvader_ClasseObjetSpatial import ObjetSpatial

#Creation de la classe
class Jeu():
    '''Permet la creation de l'instance du jeu, ainsi que de definir les methodes necessaires
    au traitement des donnees durant le jeu'''
    def __init__(self):
        '''Initialise l'instance du jeu'''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [281, 572], (25, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation des listes des entitees autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []
        self.entity = self.ennemisspeciaux + self.ennemis + self.tirs + self.blocs

        #Creation des blocs
        self.fCreationBlocs()

        #Creation de la premiere vague d'ennemi
        self.fCreationVague()

        #Creation des reperes de mmouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemidir = 1

        #Creation des etats de fonctionnement
        self.run = False
        self.gameover = False

    #Creation des methodes
    #Methodes de gestion des entitees
    def fCreation(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Creation d'un objet spatial et ajout a la liste des entitees du jeu'''
        #Creation de l'entitee
        objet = ObjetSpatial(type, vie, valeur, position, hitbox, vitesse)
        #Ajout dans la liste des entitees correspondantes
        self.fActionListe(objet, 'append')
    
    def fSuppression(self, objet):
        '''Supprime l'objet de la liste des entitees si sa vie tombe a 0 et ajoute ses points a Totpts'''
        if objet.vie <= 0:
            self.Totpts += objet.valeur
            self.fActionListe(objet, 'remove')
    
    def fCollision(self, objet):
        '''Verifie si la hitbox de l'objet rencontre une autre hitbox, si oui enleve une vie aux deux objets'''
        for entity in self.entity:
            collision = False
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
        '''Modifie la position d'un objet en fonction de sa vitesse, de la direction et du sens souhaitee.
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
        for y in [50, 90, 130, 170, 210, 250, 290, 330]:
            for x in [10, 60, 110, 160, 210, 260, 310, 360, 410]:
                self.fCreation(-2, 1, 100, [x, y], (25, 30), [5, 10])
    
    def fCreationBlocs(self):
        '''Creer tous les blocs de protection a des positions precises'''
        for bloc in [60, 260, 460]:
            for y in [532, 541, 550]:
                for x in [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]:
                    self.fCreation(0, 1, 0, [bloc + x, y], (8, 8), [0, 0])

    #Methode de fonctionnement
    def fReset(self):
        '''Remets a leur valeur d'origine tous les parametres du jeu'''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [281, 572], (25, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation des listes des entitees autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []
        self.entity = self.ennemisspeciaux + self.ennemis + self.tirs + self.blocs

        #Creation des blocs
        self.fCreationBlocs()

        #Creation de la premiere vague d'ennemi
        self.besoinVague = True
        self.fCreationVague()

        #Creation des reperes de mmouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemidir = 1

        #Creation des etats de fonctionnement
        self.run = False
        self.gameover = False
    
    def fActionListe(self, objet, action):
        '''Permet en fonction de l'action choisit ('remove' ou 'append') d'ajouter ou
        d'enlever l'objet a la liste correspondante a son type'''
        cible = self.ennemis
        if objet.type == 0:
            cible = self.blocs
        elif objet.type == -1:
            cible = self.tirs
        elif objet.type == -2:
            cible = self.ennemis
        elif objet.type == -3:
            cible = self.ennemisspeciaux
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