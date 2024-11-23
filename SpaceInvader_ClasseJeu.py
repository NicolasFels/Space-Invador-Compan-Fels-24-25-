'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Realiser un classe Jeu permettant de generer et gerer les donnees du jeu;
Fait: Initialisation du jeu;
    methode de creation des entitees;
    methode de suppression des entitees si plus de vie;
    methode de deplacement;
    methode pour reagir aux input du joueur;
    methode pour gerer les collisions;
    methode pour gerer le score;
    methode pour reset les donnees du jeu;
A faire: Realiser les methodes de gestion de tour et d'excecution du jeu;
    tester les differentes methodes creer et lister comme faites apres celle de creation;
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
        
        #Creation de la liste des entitees autres que le joueur
        self.entity = []

        #Creation des lignes ennemis
        self.lignespeciaux = []
        self.ligne1 = []
        self.ligne2 = []
        self.ligne3 = []
        self.ligne4 = []
        self.ligne5 = []
        self.ligne6 = []
        self.ligne7 = []

        #Creation des etats de fonctionnement
        self.gameover = False

    #Creation des methodes
    #Methodes de gestion des entitees
    def fCreation(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Creation d'un objet spatial et ajout a la liste des entitees du jeu'''
        #Creation de l'entitee
        objet = ObjetSpatial(type, vie, valeur, position, hitbox, vitesse)
        #Ajout dans la liste des entitees
        self.entity.append(objet)
    
    def fSuppression(self, objet):
        '''Supprime l'objet de la liste des entitees si sa vie tombe a 0 et ajoute ses points a Totpts'''
        if objet.vie == 0:
            self.Totpts += objet.valeur
            self.entity.remove(objet)
    
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
    
    #Methode de fonctionnement
    def fReset(self):
        '''Remets a leur valeur d'origine tous les parametres du jeu'''
        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [100, 100], (50, 30), [5, 0])   #Valeurs de tests amener a changer
        
        #Creation de la liste des entitees autres que le joueur
        self.entity = []

        #Creation des lignes ennemis
        self.lignespeciaux = []
        self.ligne1 = []
        self.ligne2 = []
        self.ligne3 = []
        self.ligne4 = []
        self.ligne5 = []
        self.ligne6 = []
        self.ligne7 = []

        #Creation des etats de fonctionnement
        self.gameover = False