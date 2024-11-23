'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Realiser un classe Jeu permettant de generer et gerer les donnees du jeu;
Fait: Initialisation du jeu;
    methode de creation des entitees;
    methode de creation de vague;
    methode de suppression des entitees si plus de vie;
    methode de deplacement;
    methode de mouvement des ennemis et des tirs;
    methode pour gerer les collisions;
    methode pour reset les donnees du jeu;
A faire: Realiser les methodes de gestion de tour et d'excecution du jeu;
    realiser methode de tir pour les ennemis;
    reflechir sur option de start/stop/reprise du jeu;
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
        self.joueur = ObjetSpatial(1, 3, 0, [281, 572], (50, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation des listes des entitees autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []

        #Creation de la premiere vague d'ennemi
        self.besoinVague = True
        self.fCreationVague()

        #Creation des reperes de mmouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemiou = 0

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
        if objet.vie == 0:
            self.Totpts += objet.valeur
            self.fActionListe(objet, 'remove')
    
    def fCollision(self, objet1, objet2):
        '''Verifie si les hitbox de 2 objet se rencontre, si oui enleve une vie au deux objets'''
        collision = False
        #Tests s'il y a collision entre 2 objets
        if objet1.position[0] <= objet2.position[0] and objet2.position[0] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        elif objet1.position[0] <= objet2.position[0] + objet2.taille[0] and objet2.position[0] + objet2.taille[0] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        elif objet1.position[1] <= objet2.position[1] and objet2.position[1] <= objet1.position[1] + objet1.taille[1]:
            collision = True
        elif objet1.position[1] <= objet2.position[1] + objet2.taille[1] and objet2.position[1] + objet2.taille[1] <= objet1.position[0] + objet1.taille[0]:
            collision = True
        #En cas de collision enleve une vie aux 2 objets
        if collision == True:
            objet1.vie -= 1
            objet2.vie -= 1

    def fDeplacement(self, objet, direction : int, sens : int):
        '''Modifie la position d'un objet en fonction de sa vitesse, de la direction et du sens souhaitee.
        direction : 0 pour les x, 1 pour les y
        sens: -1 pour la gauche ou le haut, 1 pour la droite ou le bas
        '''
        #Deplacement dans les donnees de l'objet
        objet.position[direction] += sens * objet.vitesse[direction]
        if objet.position[direction] < 0:
            objet.position[direction] = 0
        elif 612 < objet. position[direction] + objet.hitbox[direction]:
            objet.position[direction] = 612
        if objet.type == -1 and objet.position[direction] in [0, 612]:
            objet.vie -= 1

    def fTrouverRepere(self, extremum):
        '''Trouve l'ennemi avec la position en x la plus faible ou la plus grande.
        extremum: 1 pour la gauche, -1 pour la droite 
        '''
        for entity in self.ennemis:
            if entity.position[0] <= extremum * self.repere.position[0]:
                self.repere = entity
        
    def fMouvementEnnemi(self):
        '''Fait se deplacer tous les ennemis dans la base de donnees, en fonction de ennemiou
        va a droite(0), a gauche(1) ou descend(2)
        '''
        if self.ennemiou == 0:
            for entity in self.ennemis:
                self.fDeplacement(entity, 0, 1)
            if self.ennemirepere.position[0] + self.ennemirepere.hitbox[0] == 602:
                self.ennemiou = 1
        elif self.ennemiou == 1:
            for entity in self.ennemis:
                self.fDeplacement(entity, 0, -1)
            if self.ennemirepere.position[0] == 10:
                if self.ennemirepere.position[1] + self.ennemirepere.hitbox[1] == 602:
                    self.ennemiou = 0
                else:
                    self.ennemiou = 2
        elif self.ennemiou == 2:
            for entity in self.ennemis:
                self.fDeplacement(entity, 1, 1)
        
    def fMouvementTir(self):
        '''Fait se deplacer les tirs dans la base de donnees'''
        for entity in self.tirs:
            self.fDeplacement(entity, 1, 1)

    def fCreationVague(self):
        '''Si la liste des ennemis est vide, creer 8 lignes de 6 ennemis a partir des coordonnees (10, 10).
        Chaque ennemi est espace de 30 avec son voisin et chaque ligne de 10.
        '''
        if self.besoinVague == True:
            for y in [50, 90, 130, 170, 210, 250, 290, 330]:
                for x in [10, 90, 170, 250, 330, 410]:
                    self.fCreation(-2, 1, 100, [x, y], (50, 30), [5, 10])

    #Methode de fonctionnement
    def fReset(self):
        '''Remets a leur valeur d'origine tous les parametres du jeu'''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [100, 100], (50, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation des listes des entitees autres que le joueur
        self.ennemisspeciaux = []
        self.ennemis = []
        self.tirs = []
        self.blocs = []

        #Creation de la premiere vague d'ennemi
        self.fCreationVague()

        #Creation des reperes de mmouvements ennemis
        self.ennemirepere = self.ennemis[0]
        self.ennemiou = 0

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
        elif action == 'append':
            cible.append(objet)