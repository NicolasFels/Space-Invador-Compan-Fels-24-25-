'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Realiser un classe Jeu permettant de generer et gerer l'instance du jeu ainsi que toutes les actions et reactions;
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
    '''Permet la creation de l'instance du jeu, ainsi que de definir les methodes necessaires au fonctionnement du jeu'''
    def __init__(self, visuel):
        '''Initialise l'instance du jeu'''
        #Lien entre l'instance de jeu et la fenetre graphique
        self.visuel = visuel

        #Mise a 0 du score
        self.Totpts = 0

        #Creation et affichage du joueur
        self.joueur = ObjetSpatial(1, 3, 0, [100, 100], (50, 30), [2, 0])   #Valeurs de tests amener a changer
        self.visuel.fAffichage(self.joueur)
        
        #Creation de la liste des entitees autres que le joueur
        self.entity = []
        self.fCreation(-2, 1, 100, [300, 300], (50, 30), [2, 40])

    #Creation des methodes
    def fCreation(self, type : int, vie : int, valeur : int, position : list, hitbox : tuple, vitesse : list):
        '''Creation d'un objet spatial et ajout a la liste des entitees du jeu'''
        #Creation de l'entitee
        objet = ObjetSpatial(type, vie, valeur, position, hitbox, vitesse)
        #Ajout dans la liste des entitees
        self.entity.append(objet)
        #Affichage dans la fenetre graphique
        self.visuel.fAffichage(objet)

    def fSuppression(self, objet):
        '''Supprime l'objet de la liste des entitees si sa vie tombe a 0'''
        if objet.vie == 0:
            self.entity.remove(objet)
            self.visuel.fSupprimer(objet)

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
        #Deplacement dans la fenetre graphique
        self.visuel.fDeplace(objet, direction, sens)
    
    def fActionJoueur(self, action):
        '''Active une reaction en fonction d'une action du joueur sur le clavier'''
        if action == 'LEFT':
            self.fDeplacement(self.joueur, 0, -1)
        elif action == 'RIGHT':
            self.fDeplacement(self.joueur, 0, 1)
        elif action == 'Space':
            self.fCreation(-1, 1, 0, [self.joueur.position[0] + 20, self.joueur.position[1] - 6], (5, 5), [0, 10])

    def fCollision(self, objet1, objet2):
        '''Verifie si les hitbox de 2 objet se rencontre, si oui enleve une vie au deux objets'''
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
            objet1.vie -= 1
            objet2.vie -= 1

    def fScore(self, Newpts : int):
        '''Permet de modifier le score, puis de changer son affichage dans la fenetre graphique'''
        self.Totalpts += Newpts
        self.visuel.score.set('Score actuel: ' + str(self.Totalpts))
    
    def fReset(self):
        '''Permet de reset toutes les donnees du jeu, ainsi que l'affichage dans la fenetre graphique'''
        #Suppression de toutes les donnees et de tous les objets afficher
        for objet in self.entity:
            self.visuel.fSupprimer(objet)
        self.visuel.fSupprimer(self.joueur)
        #Mise a 0 des parametres du jeu
        self.Totpts = 0
        self.joueur = ObjetSpatial(1, 3, 0, [100, 100], (50, 30), [2, 0])   #Valeurs de tests amener a changer
        self.visuel.fAffichage(self.joueur)
        self.entity = []
        #Mis a l'etat False du parametre NewGame pour signifier qu'on a creert un nouveau jeu
        self.visuel.NewGame = False