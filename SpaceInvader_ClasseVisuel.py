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
A faire: Realisation des methode de gestion de tour et d'execution du jeu;
    voir si on modifie l'apparence des boutons;
    reflechir sur ajout d'option start/stop/reprise du jeu en cours en lien avec la classe Jeu;
    reflechir a differentes ameliorations possibles;
'''
#Bibliotheque standard
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar, Toplevel, LabelFrame, Event

#Bibliotheque personnelle
from SpaceInvader_ClasseObjetSpatial import ObjetSpatial

#Creation de la classe Visuel
class Visuel():
    '''Permet la creation d'une fenetre visuelle de jeu'''
    def __init__(self, mg):
        '''Initialisation de la fenetre'''
        #Definition des caracteristiques de base de la fenetre
        self.mv = Tk()
        self.mv.title('Compan and Fels: Space Invaders')
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
        self.labelScore = Label(self.mv, textvariable = self.score)             #Amener a changer selon comment est gerer le score
        self.labelBestScore = Label(self.mv, textvariable = self.bestscore)     #Amener a changer selon comment est gerer le score

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
        self.labelScore.pack(side = 'top', pady =30)
        self.labelBestScore.pack(side = 'top', padx = 20)                       #Amener a changer en fonction du rendu

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

        #Apparition des ennemis sur le Canvas
        self.fAffichageVague()
        
        #Creation des evenements
        self.mv.bind('<Key>', self.fActionJoueur)
        #Lancement de la fenetre
        self.mv.mainloop()

    #Creation des methodes
    #Methode propre aux menus, boutons et labels
    def fCreate_regle(self):
        '''Creation d'une fenetre contenant les regles du jeu depuis le MenuPropos'''
        regle = Toplevel(self.mv)
        regle.title('Regles du jeu')
        TitreRegle = LabelFrame(regle, text = "Regles du jeu", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Vous savez jouer, non ?").pack()

    def fCreate_nous(self):
        '''Creation d'une fenetre contenant des informations sur nous depuis le MenuPropos'''
        nous = Toplevel(self.mv)
        nous.title('A propos de nous')
        TitreRegle = LabelFrame(nous, text = "A propos de nous", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Nico et Nono").pack()

    def fNewGame(self):
        '''Associer au bouton NEWGAME, met la valeur True au parametre NewGame.'''
        for id in self.entityId:
            self.GameZone.delete(id)
        self.mg.fReset()
        self.valeurscore = 0
        self.fScore()

    def fScore(self):
        '''Modifie en temps reel le score affiche du joueur'''
        self.valeurscore = self.mg.Totpts
        self.score.set('Score actuel: ' + str(self.valeurscore))
    
    def fBestScore(self):
        '''Modifie le meilleur score en temps reel s'il est inferieur au score actuel du joueur'''
        if self.valeurbestscore < self.valeurscore:
            self.valeurbestscore = self.valeurscore
            self.bestscore.set('Score actuel: ' + str(self.valeurbestscore))
    
    #Methodes standards propre au Canvas GameZone
    def fAffichage(self, objet):
        '''Affiche l'objet sur le Canvas GameZone'''
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
        objet.id = self.GameZone.create_image(objet.position[0], objet.position[1],anchor = 'nw', image = apparence)
        self.entityId.append(objet.id)
    
    def fDeplace(self, objet, direction : int, sens : int):
        '''Deplace l'objet sur le Canvas GameZone selon une direction et un sens precis'''
        if direction == 0:
            self.GameZone.move(objet.id, sens * objet.vitesse[direction], 0)
        else:
            self.GameZone.move(objet.id, 0, sens * objet.vitesse[direction])
    
    def fSupprimer(self, objet):
        '''Supprime l'objet de l'écran'''
        self.entityId.remove(objet.id)
        self.GameZone.delete(objet.id)
    
    #Methodes avances propre au Canvas GameZone
    def fMoveEnnemi(self):
        '''Deplace tous les ennemis sur le Canvas GameZone selon une direction et un sens precis'''
        if self.mg.ennemidir == 0:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, 1)
            if self.mg.ennemirepere.position[0] + self.ennemirepere.hitbox[0] == 602:
                self.mg.ennemidir = 1
        elif self.mg.ennemidir == 1:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, -1)
            if self.mg.ennemirepere.position[0] == 10:
                if self.mg.ennemirepere.position[1] + self.mg.ennemirepere.hitbox[1] == 602:
                    self.mg.ennemidir = 0
                else:
                    self.mg.ennemidir = 2
        elif self.mg.ennemidir == 2:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 1, 1)
            self.mg.ennemidir = 0
    
    def fMoveTir(self):
        '''Deplace tous les tir sur le Canvas GameZone sur l'axe y et dans le sens precise dans leur vitesse'''
        for entity in self.mg.tirs:
            self.fDeplace(entity, 1, 1)

    def fAffichageVague(self):
        '''Affiche tous les ennemis de la nouvelle vague sur le Canvas GameZone'''
        if self.mg.besoinVague == True:
            for entity in self.mg.ennemis:
                self.fAffichage(entity)
            self.mg.besoinVague = False

    def fAffichageBlocs(self):
        '''Affiche les blocs de protections au debut du jeu'''
        for blocs in self.mg.blocs:
            self.fAffichage(blocs)
    
    #Methode d'ecoute des inputs du joueur
    def fActionJoueur(self, event):
        action = event.keysym
        print(action)
        if action == 'Left':
            self.mg.fDeplacement(self.mg.joueur, 0, -1)
            self.fDeplace(self.mg.joueur, 0, -1)
        elif action == 'Right':
            self.mg.fDeplacement(self.mg.joueur, 0, 1)
            self.fDeplace(self.mg.joueur, 0, 1)
        elif action == 'space':
            self.mg.fCreation(-1, 1, 0, [self.mg.joueur.position[0] + 20, self.mg.joueur.position[1] - 6], (5, 5), [0, -10])
            self.fAffichage(self.mg.tirs[-1])
    
    #Methode gestion du tour
    