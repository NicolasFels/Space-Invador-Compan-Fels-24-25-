'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 25/11/2024
But: Realiser une classe permettant la creation d'une fenetre graphique de jeu;
Fait: Initialisation de la fenetre avec tous les parametres actuellement utile;
    methodes des boutons, labels et menus;
    methodes standard propre au Canvas GameZone;
    debut des methodes avances propre au Canvas GameZone;
    methode d'ecoute du clavier fAction;
    toutes les images sont importer;
    methode start and stop;
    methode gestion de tour;
A faire: Reflechir a differentes ameliorations possibles;
'''
#Bibliotheque standard
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar, Toplevel, LabelFrame, Event
from random import randint

#Bibliotheque personnelle
from SpaceInvader_ClasseObjetSpatial import ObjetSpatial

#Creation de la classe Visuel
class Visuel():
    '''Permet la creation d'une fenetre visuelle de jeu'''
    def __init__(self, mg):
        '''Initialisation de la fenetre'''
        #Definition des caracteristiques de base de la fenetre
        self.mv = Tk()
        self.mv.title('Compan and Fels: Candy Invaders')
        self.mv.geometry('612x700')

        #Lien entre le jeu et la fenetre graphique
        self.mg = mg

        #Creation des boutons
        self.buttonQuit = Button(self.mv, text = "QUITTER", command = self.mv.destroy)
        self.buttonNewGame = Button(self.mv, text = "NEW GAME", command = self.fNewGame)

        #Creation des labels de score
        self.valeurscore = 0
        self.valeurbestscore = 0
        self.score = StringVar()
        self.bestscore = StringVar()
        self.fScore()
        self.fBestScore()
        self.labelScore = Label(self.mv, textvariable = self.score)     
        self.labelBestScore = Label(self.mv, textvariable = self.bestscore)

        #Creation du menu
        self.MenuBar = Menu(self.mv)
        self.MenuFichier = Menu(self.MenuBar, tearoff = 0)
        self.MenuPropos = Menu(self.MenuBar, tearoff = 0)
        self.MenuBar.add_cascade(label = 'Fichier', menu = self.MenuFichier)
        self.MenuBar.add_cascade(label = 'A propos', menu = self.MenuPropos)
        self.MenuFichier.add_command(label = 'Quitter', command = self.mv.destroy)
        self.MenuPropos.add_command(label = 'Regles du jeu', command = self.fCreate_regle)
        self.MenuPropos.add_command(label = 'Sur nous', command = self.fCreate_nous)
        self.mv.config(menu = self.MenuBar)

        #Creation du Canvas
        self.background = PhotoImage(file = 'SpaceInvader_Image/nappe.png')
        self.GameZone = Canvas(self.mv, height = 612, width = 612)
        self.GameZone.create_image(0, 0, anchor = 'nw', image = self.background)

        #Positionnement des widget
        self.GameZone.pack(side = "bottom")
        self.buttonNewGame.pack(side = "left", pady = 10, padx = 30)
        self.buttonQuit.pack(side = "right", pady = 10, padx = 30)
        self.labelScore.pack(side = 'top', pady =10)
        self.labelBestScore.pack(side = 'top')

        #Creation des apparences des entitees
        self.joueur = PhotoImage(file = 'SpaceInvader_Image/tooth.png')
        self.ennemi = PhotoImage(file = 'SpaceInvader_Image/candy.png')
        self.ennemispecial = PhotoImage(file = 'SpaceInvader_Image/lolipop.png')
        self.tir = PhotoImage(file = 'SpaceInvader_Image/raisin.png')
        self.bloc = PhotoImage(file = 'SpaceInvader_Image/chocolate.png')

        #Creation d'une liste des entitees affichee
        self.entityId = []

        #Apparition du joueur sur le Canvas GameZone
        self.fAffichage(self.mg.joueur)

        #Apparition des blocs de protections
        self.fAffichageBlocs()

        #Apparition des ennemis sur le Canvas
        self.fAffichageVague()
        
        #Creation des evenements
        self.mv.bind('<Key>', self.fActionJoueur)
        
        #Lancement du tour
        self.fGestionTour()

        #Lancement de la fenetre
        self.mv.mainloop()

    #Creation des methodes
    #Methode de fonctionnement de la fenetre
    def fCreate_regle(self):
        '''Creation d'une fenetre contenant les regles du jeu depuis le MenuPropos'''
        regle = Toplevel(self.mv)
        regle.title('Regles du jeu')
        TitreRegle = LabelFrame(regle, text = "Regles du jeu", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Tirez sur les Sucreries afin de les faire disparaître avant que celles-ci atteignent votre Dent. Protégez-vous à l'aide des tablettes de chocolat !").pack()
        Label(TitreRegle, text = "Votre dent possède trois vies et en perd une a chaque contact avec une sucrerie ennemi. De plus l'élimination d'une sucrerie classique vous ocroiera").pack()
        Label(TitreRegle, text = "100 points, celle d'une sucrerie spéciale le DOUBLE. Mais faites attention les sucreries n'en finissent pas d'apparaître et elle deviennent de plus").pack()
        Label(TitreRegle, text = "en plus savoureuse ! A chauqe vague détruite le nombre de vie des sucreries classiques augmentent, à vous de voir jusqu'où vous pourrez protéger votre dent.").pack()
        Commande = LabelFrame(regle, text = "Commandes", padx = 20, pady = 20)
        Commande.pack(fill = 'both', expand = 'yes')
        Label(Commande, text = "- utiliser les flèches directionnelles pour vous déplacer (le joueur ne se déplace que à gauche ou à droite)").pack()
        Label(Commande, text = "- utiliser la barre espace pour tirer").pack()
        Label(Commande, text = "- utiliser la touche entrée (Return pour tkinter) pour mettre le jeu en pause et le lancer au début").pack()
        
        
        

    def fCreate_nous(self):
        '''Creation d'une fenetre contenant des informations sur nous depuis le MenuPropos'''
        nous = Toplevel(self.mv)
        nous.title('A propos de nous')
        TitreRegle = LabelFrame(nous, text = "A propos de nous", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Créé par COMPAN Nolwenn et FELS Nicolas").pack()

    def fNewGame(self):
        '''Associer au bouton NEWGAME, met la valeur True au parametre NewGame.'''
        #Supprime toutes les entitees a l'ecran
        for id in self.entityId:
            self.GameZone.delete(id)
        #Reset les donnees du jeu et du visuel a l'aide des fonctions de reset
        self.mg.fReset()
        self.fResetVisuel()

    def fScore(self):
        '''Modifie en temps reel le score affiche du joueur'''
        self.valeurscore = self.mg.Totpts                               #le score est egale au total des points du jeu
        self.score.set('Score actuel: ' + str(self.valeurscore))        #met a jour la variable du texte du score
    
    def fBestScore(self):
        '''Modifie le meilleur score en temps reel s'il est inferieur au score actuel du joueur.
        A le meme fonctionnement que fScore(), mais uniquement quand le nouveau score est superieur au meilleur score
        enregistre. Le meilleur score est propre a la fenetre et n'est pas sauvegarde entre chaque fenetre.'''
        if self.valeurbestscore < self.valeurscore:
            self.valeurbestscore = self.valeurscore
            self.bestscore.set('Best score: ' + str(self.valeurbestscore))

    def fResetVisuel(self):
        '''Reset le visuel'''
        #Mise a 0 du label score
        self.fScore()

        #Mise a 0 de la liste des entitees affichee
        self.entityId = []

        #Apparition du joueur sur le Canvas GameZone
        self.fAffichage(self.mg.joueur)

        #Apparition des blocs de protections
        self.fAffichageBlocs()

        #Apparition des ennemis sur le Canvas
        self.fAffichageVague()
        
        #Si la ligne suivante est decommente la vitesse du jeu va augmenter a chaque NewGame
        #self.fGestionTour()
    
    #Methodes standards propre au Canvas GameZone
    def fAffichage(self, objet):
        '''Affiche l'objet sur le Canvas GameZone'''
        #Test le type de l'entitee pour savoir qu'elle image associer
        if objet.type == 1:
            apparence = self.joueur
        elif objet.type == 0:
            apparence = self.bloc
        elif objet.type == -1:
            apparence = self.tir
        elif objet.type == -2:
            apparence = self.ennemi
        elif objet.type == -3:
            apparence = self.ennemispecial
        #Lie le parametre id de l'entitee a son image a l'ecran puis l'ajoute dans la liste comptenant les id des entitees a l'ecran
        objet.id = self.GameZone.create_image(objet.position[0], objet.position[1],anchor = 'nw', image = apparence)
        self.entityId.append(objet.id)
    
    def fDeplace(self, objet, direction : int, sens : int):
        '''Deplace l'objet sur le Canvas GameZone selon une direction et un sens precis'''
        #Gere les deplacements sont sur l'axe des x
        if direction == 0:
            self.GameZone.move(objet.id, sens * objet.vitesse[direction], 0)            #Deplacement a l'ecran
            self.mg.fDeplacement(objet, direction, sens)                                #Deplacement dans les donnees
            #Test pour savoir si l'entitee sort de la zone de jeu, soit (10, 602) pour les x et y
            #Si l'entitee sort de la zone de jeu effectue un mouvement pour la remettre dans la zone de jeu et met sa position aux limites de la zone
            if objet.position[direction] < 10:
                self.GameZone.move(objet.id, - sens * abs(objet.position[direction] - 10), 0)
                objet.position[direction] = 10
            elif 602 < objet. position[direction] + objet.hitbox[direction]:
                self.GameZone.move(objet.id, - sens * abs(objet.position[direction] - (602 - objet.hitbox[direction])), 0)
                objet.position[direction] = 602 - objet.hitbox[direction]
        #Gere les deplacements sur l'axe des y, meme principe que pour l'axe des x
        else:
            self.GameZone.move(objet.id, 0, sens * objet.vitesse[direction])
            self.mg.fDeplacement(objet, direction, sens)
            if objet.position[direction] < 10:
                self.GameZone.move(objet.id, 0, - sens * abs(objet.position[direction] - 10))
                objet.position[direction] = 10
            elif 602 < objet. position[direction] + objet.hitbox[direction]:
                self.GameZone.move(objet.id, 0, - sens * abs(objet.position[direction] - (602 - objet.hitbox[direction])))
                objet.position[direction] = 602
            #Si l'entitee est un tir et qu'elle sort des limites, alors lui retire une vie. C'est equivalent a la detruire
            if objet.type == -1 and objet.position[direction] in [10, 602]:
                objet.vie -= 1
    
    def fSupprimer(self, objet):
        '''Supprime l'objet si sa vie tombe a 0'''
        self.mg.fSuppression(objet)
        if objet.vie <= 0:
            self.entityId.remove(objet.id)
            self.GameZone.delete(objet.id)
    
    #Methodes avances propre au Canvas GameZone
    def fMoveEnnemi(self):
        '''Deplace tous les ennemis sur le Canvas GameZone selon une direction et un sens precis.
        -1 a gauche, 0 en bas, 1 a droite'''
        #Test le sens de deplacement des ennemis classiques
        if self.mg.ennemidir == 1:
            #Deplcae tous les ennemis classique dans ce sens
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, 1)
            #Regarde si l'ennemi classique de repere a atteint la limite a droite
            if self.mg.ennemirepere.position[0] + self.mg.ennemirepere.hitbox[0] == 602:
                #Change le sens de deplcament vers la gauche pour le prochain tour
                self.mg.ennemidir = -1
        elif self.mg.ennemidir == -1:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, -1)
            #Regarde si l'ennemi classique de repere a atteint la limite a gauche
            if self.mg.ennemirepere.position[0] == 10:
                #Regarde si l'ennemi repere a atteint la limite basse, si oui change le sens de deplacement vers la droite pour le prochain tour, si non vers le bas
                if self.mg.ennemirepere.position[1] + self.mg.ennemirepere.hitbox[1] == 602:
                    self.mg.ennemidir = 1
                else:
                    self.mg.ennemidir = 0
        elif self.mg.ennemidir == 0:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 1, 1)
            #Change le sens de deplacement vers la droite pour le prochain tour
            self.mg.ennemidir = 1
    
    def fMoveEnnemiSpeciaux(self):
        '''Deplace tous les ennemis speciaux sur le Canvas GameZone selon une direction et un sens precis.
        -1 a gauche, 1 a droite '''
        #Test le sens de deplacement des ennemis speciaux
        if self.mg.ennemisspeciaux != [] and self.mg.ennemisspeciauxdir == 1:
            #Deplace tous les ennemis speciaux. Il n'y a qu'un ennemi special, mais si on veut en ajouter plusieurs l'adaptation est deja faite
            for entity in self.mg.ennemisspeciaux:
                self.fDeplace(entity, 0, 1)
            #Regarde si les ennemis speciaux ont atteint la limite droite et change le sens de deplacement en consequence
            if self.mg.ennemisspeciaux[0].position[0] + self.mg.ennemisspeciaux[0].hitbox[0] == 602:
                self.mg.ennemisspeciauxdir = -1
        elif self.mg.ennemisspeciaux != [] and self.mg.ennemisspeciauxdir == -1:
            for entity in self.mg.ennemisspeciaux:
                self.fDeplace(entity, 0, -1)
            #Meme principe que pour la droite, mais en plus supprime le dernier ennemi special de la liste donc celui de gauche
            if self.mg.ennemisspeciaux[-1].position[0] == 10:
                self.mg.ennemisspeciauxdir = 1
                self.GameZone.delete(self.mg.ennemisspeciaux[-1].id)
                self.mg.entity.remove(self.mg.ennemisspeciaux[-1])
                self.mg.ennemisspeciaux.remove(self.mg.ennemisspeciaux[-1])
                
    def fMoveTir(self):
        '''Deplace tous les tir sur le Canvas GameZone sur l'axe y et dans le sens precise dans leur vitesse'''
        #Parcourt la liste des tirs et les deplaces tous, le sens est en positif car la vitesse des tirs est mise en négative pour ceux du joueur et positive pour ceux des ennemis
        for entity in self.mg.tirs:
            self.fDeplace(entity, 1, 1)

    def fAffichageVague(self):
        '''Affiche tous les ennemis de la nouvelle vague sur le Canvas GameZone'''
        for entity in self.mg.ennemis:
            self.fAffichage(entity)

    def fAffichageBlocs(self):
        '''Affiche les blocs de protections au debut du jeu'''
        for blocs in self.mg.blocs:
            self.fAffichage(blocs)

    def fAffichageEnnemiSpeciaux(self):
        '''Affiche l'ennemi special en haut du Canvas GameZone'''
        if self.mg.ennemisspeciaux == [] and randint(0,100) == 42:          #Test s'il n'y a pas d'ennemi special en jeu et si une condition random est respectee
            self.mg.fCreationEnnemiSpecial()                                #Creer les donnees d'un ennemi special
            self.fAffichage(self.mg.ennemisspeciaux[0])                     #Affiche l'ennemi special
    
    #Methode d'ecoute des inputs du joueur
    def fActionJoueur(self, event):
        '''Determine les actions du personnage joueur en fonction des input du joueur'''
        action = event.keysym
        print(action)
        if action == 'Left' and self.mg.run == True:
            self.fDeplace(self.mg.joueur, 0, -1)
        elif action == 'Right' and self.mg.run == True:
            self.fDeplace(self.mg.joueur, 0, 1)
        elif action == 'space' and self.mg.run == True and self.mg.tirpossible == True:
            #self.mg.fTirPossible()                                                             Tentative infructueuse pour introduire un delais entre les tirs du joueur
            self.mg.fCreation(-1, 1, 0, [self.mg.joueur.position[0] + 13, self.mg.joueur.position[1] - 6], (5, 5), [0, -10])
            self.fAffichage(self.mg.tirs[-1])
            #self.mv.after(2000, self.mg.fTirPossible())                                        Tentative infructueuse pour introduire un delais entre les tirs du joueur
        if action == 'Return':
            if self.mg.run == True:
                self.mg.run = False
                print("PAUSE")
            else:
                self.mg.run = True
                print("START")

    #Methode gestion du tour
    def fGestionTour(self):
        '''Gere le deroulement d'un tour, puis apres un certain temps se reactive.'''
        if self.mg.gameover == False:                   #Regarde si le joueur n'a pas perdu
            if self.mg.run == True:                     #Regarde si le jeu n'est pas en pause
                self.fAffichageEnnemiSpeciaux()         #Regarde si un ennemi special peut etre cree et si les conditions sont reunis le cree
                self.mg.fTrouverRepere()                #Trouve l'ennemi classique de repere
                self.fMoveEnnemiSpeciaux()              #Deplace les ennemis speciaux
                self.fMoveEnnemi()                      #Deplace les ennemis classique grace a l'ennemi de repere
                self.fMoveTir()                         #Deplace les tirs
                self.mg.fCollision(self.mg.joueur)      #Verifie si le joueur entre en collision avec une entitee   
                for entity in self.mg.entity:           #Verifie les collisions de toutes les autres entitees
                        self.mg.fCollision(entity)
                        self.fSupprimer(entity)         #Supprime les entitees ennemis n'ayant plus de vie
                self.fScore()                           #Actualise le score
                self.fBestScore()                       #Actualise le best score
                self.mg.fGameOver()                     #Regarde si le joueur a perdu et change l'etat de gameover en consequence
                if self.mg.ennemis == []:               #Si la vague actuelle d'ennemi est detruite en fabrique une nouvelle
                    self.mg.fCreationVague()
                    self.fAffichageVague()
        self.mv.after(100, self.fGestionTour)           #Rappel la fonction apres un certain temps pour jouer un nouveau tour
    