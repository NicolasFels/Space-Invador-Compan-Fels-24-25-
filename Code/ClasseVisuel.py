'''
Nicolas Fels
Derniere modification: 20/11/2024
But: Creation d'une classe Visuel pour creer des fenetres
    ->boutons QUITTER et NEWGAME
    ->label SCORE variable
    ->canvas GameZone avec une image de fond
    ->menubar avec une zone Fichier et une zone A propos
A faire:
    ->resoudre le probleme de l'image
    ->remplir les textes des menus
'''
#Bibliotheque
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar, Toplevel, LabelFrame, Frame

#Creation de la classe
class Visuel():
    '''Classe permettant la creation d'une fenetre'''
    def __init__(self):
        
        #Definition des caracteristiques de base de la fenetre
        self.mv = Tk()
        self.mv.title('Compan and Fels: Space Invaders')
        self.mv.geometry('612x650')                     #taille de la fenetre peut changer en fonction de l'image de fond

        #Creation des boutons
        self.buttonQuit = Button(self.mv, text = "QUITTER", command = self.mv.destroy)
        self.buttonNewGame = Button(self.mv, text = "NEW GAME")

        #Creation des labels 
        self.Totalpts = 0
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
        self.GameZone = Canvas(self.mv, height = 612, width = 612, background = 'black')
        #background = PhotoImage(file = '../image/')                        Probleme pour l'image -> trouver une image en .png
        #self.GameZone.create_image(0, 0, anchor = 'nw', image = background)

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
