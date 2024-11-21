'''
Nicolas Fels
Derniere modification: 21/11/2024
But: Creation d'une classe Visuel pour creer des fenetres
    ->boutons QUITTER et NEWGAME
    ->label SCORE variable
    ->canvas GameZone avec une image de fond
    ->menubar avec une zone Fichier et une zone A propos
A faire:
    ->comprendre pk fAffiche ne fonctionne pas
    ->mettre les bonnes images
    ->remplir les textes des menus
    ->faire la fonction fNewGame
'''
#Bibliotheque
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar, Toplevel, LabelFrame

#Creation de la classe
class Visuel():
    '''Classe permettant la creation d'une fenetre'''
    def __init__(self):
        
        #Definition des caracteristiques de base de la fenetre
        self.mv = Tk()
        self.mv.title('Compan and Fels: Space Invaders')
        self.mv.geometry('612x700')                     #taille de la fenetre peut changer en fonction de l'image de fond

        #Creation des boutons
        self.buttonQuit = Button(self.mv, text = "QUITTER", command = self.mv.destroy)
        self.buttonNewGame = Button(self.mv, text = "NEW GAME")

        #Creation des labels 
        self.score = StringVar()
        self.labelScore = Label(self.mv, textvariable = self.score)      #Amener a changer pour etre traiter par Jeu

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
        self.GameZone = Canvas(self.mv, height = 612, width = 612)
        self.background = PhotoImage(file = 'background.gif')                        #Probleme pour l'image -> trouver une image en .png
        self.GameZone.create_image(0, 0, anchor = 'nw', image = self.background)

        #Positionnement des widget
        self.GameZone.pack(side = "bottom")
        self.buttonNewGame.pack(side = "left", pady = 10, padx = 30)
        self.buttonQuit.pack(side = "right", pady = 10, padx = 30)
        self.labelScore.pack(side = 'top', pady =30)

    def fCreate_regle(self): # Creation des fenetres regle
        regle = Toplevel(self.mv)
        regle.title('Regles du jeu')
        TitreRegle = LabelFrame(regle, text = "Regles du jeu", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Vous savez jouer, non ?").pack()

    def fCreate_nous(self):
        nous = Toplevel(self.mv)
        nous.title('A propos de nous')
        TitreRegle = LabelFrame(nous, text = "A propos de nous", padx = 20, pady = 20)
        TitreRegle.pack(fill = 'both', expand = 'yes')
        Label(TitreRegle, text = "Nico et Nono").pack()

    def fBindKey(self, function):
        self.mv.bind('<Key>', function)
    
    def fNewGame(self):
        '''Fonction associer au bouton NEWGAME, reset la page et lance un nouveau jeu'''
        pass

    def fAffichage(self, objet):
        '''Affiche l'objet demandé'''
        if objet.type == -2:
            apparence = PhotoImage(file = 'ennemi.gif')
        elif objet.type == -1:
            apparence = PhotoImage(file = 'tir.png')
        elif objet.type == 0:
            apparence = PhotoImage(file = 'bloc.png')
        elif objet.type == 1:
            apparence = PhotoImage(file = 'joueur.png')
        objet.forme = self.GameZone.create_image(objet.position[0], objet.position[1], image = apparence)
    
    def fDeplace(self, objet, sens, direction):
        '''Deplace l'objet sur la fenetre'''
        if direction == 0:
            self.visuel.GameZone.move(objet.forme, sens*objet.vitesse[direction], 0)
        else:
            self.visuel.GameZone.move(objet.forme, 0, sens*objet.vitesse[direction])
    
    def fSupprimer(self, objet):
        '''Supprime l'objet de l'écran'''
        self.GameZone.delete(objet.forme)
        
    def mainloop(self):
        self.mv.mainloop()
