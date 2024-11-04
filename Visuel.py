"""
Nicolas FELS
04/11/2024
But: Faire la classe Fenetre du jeu space invaders
A faire:
"""

import tkinter as tk

class Visuel():
    def __init__(self,root):
        self.nom = "Space-Invaders"
        root.title(self.nom)
        self.score = tk.Label(root, text = "Score :")
        self.score.grid(column = 0, row = 0)
        self.button_jeu = tk.Button(root, text = "Nouvelle partie")
        self.button_jeu.grid(column = 1, row = 0)
        self.button_quit = tk.Button(root, text = "Quitter", command=root.destroy)
        self.button_quit.grid(column = 2, row = 0)
        self.canvas = tk.Canvas(root, width = 800, height = 800, bg = "black")
        self.canvas.grid(column = 0, columnspan = 3, row = 1)
