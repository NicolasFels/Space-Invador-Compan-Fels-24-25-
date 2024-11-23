'''
Nicolas FELS, Nolwenn COMPAN
Derniere modification: 23/11/2024
But: Realiser une classe permettant la creation d'une fenetre graphique de jeu;
Fait: Initialisation de la fenetre avec tous les parametres actuellement utile;
    methodes des boutons et menus;
    methodes propre au Canvas;
    methode d'ecoute du clavier fAction;
    methode de fonctionnement fMainloop();
A faire: Rajouter les bonnes images pour les ennemi speciaux, les tirs et les blocs;
    voir si on modifie l'apparence des boutons
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
    def __init__(self):
        '''Initialisation de la fenetre'''
        #Definition des caracteristiques de base de la fenetre
        self.mv = Tk()
        self.mv.title('Compan and Fels: Space Invaders')
        self.mv.geometry('612x700')

        #Creation des boutons
        self.buttonQuit = Button(self.mv, text = "QUITTER", command = self.mv.destroy)
        self.buttonNewGame = Button(self.mv, text = "NEW GAME", command = self.fNewGame)

        #Creation des labels 
        self.score = StringVar()
        self.labelScore = Label(self.mv, textvariable = self.score)     #Amener a changer selon comment est gerer le score

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

        #Creation des evenements et variables d'ecoute
        self.NewGame = False
        self.ActionJoueur = None
        self.mv.bind('<Key>', self.fAction)

        #Creation des apparences des entitees
        self.joueur = PhotoImage(file = 'SpaceInvader_Image/tooth.png')
        self.ennemi = PhotoImage(file = 'SpaceInvader_Image/candy.png')
        self.ennemispecial = PhotoImage(file = 'SpaceInvader_Image/candy.png')
        self.tir = PhotoImage(file = 'SpaceInvader_Image/candy.png')        #Changer l'image quand on l'aura
        self.bloc = PhotoImage(file = 'SpaceInvader_Image/candy.png')       #Changer l'image quand on l'aura

        #Creation d'une liste des entitees affichee
        self.entityId = []

    #Creation des methodes
    #Methode propre aux menus et boutons
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
        self.NewGame = True
    
    #Methode propre au Canvas
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
        '''Deplace l'objet sur la fenetre'''
        if direction == 0:
            self.visuel.GameZone.move(objet.id, sens*objet.vitesse[direction], 0)
        else:
            self.visuel.GameZone.move(objet.id, 0, sens*objet.vitesse[direction])

    def fSupprimer(self, objet):
        '''Supprime l'objet de l'écran'''
        self.GameZone.delete(objet.id)

    #Methode d'ecoute du clavier
    def fAction(self, event):
        '''Change l'attribut de l'action joueur en fonction de la touche appuyer'''
        self.ActionJoueur = event.keysym
    
    #Methode pour faire fonctionner la fenetre
    def fMainloop(self):
        '''Necessaire pour faire tourner la fenetre apres l'avoir liee au jeu'''
        self.mv.mainloop()

