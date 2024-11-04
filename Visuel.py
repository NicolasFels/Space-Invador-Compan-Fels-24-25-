"""
Nicolas FELS
04/11/2024
But: Faire la classe Fenetre du jeu space invaders
A faire:
"""
# Librairies
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label

#Classe Visuel
class Visuel():
    def __init__(self):
        self.mf = Tk()
        self.nom = "Space-Invaders"
        self.mf.title(self.nom)
        self.score = Label(self.mf, text = "Score :")
        self.score.grid(column = 0, row = 0)
        self.button_jeu = Button(self.mf, text = "Nouvelle partie")
        self.button_jeu.grid(column = 1, row = 0)
        self.button_quit = Button(self.mf, text = "Quitter", command=self.mf.destroy)
        self.button_quit.grid(column = 2, row = 0)
        self.canvas = Canvas(self.mf, width = 800, height = 800, bg = "black")
        self.canvas.grid(column = 0, columnspan = 3, row = 1)
        self.mf.mainloop()
