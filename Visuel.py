"""
Nicolas FELS
04/11/2024
But: Generer et gerer la fenetre graphique en tkinter
    ->les boutons quitter et new game
    ->les labels score
    ->le canvas avec une image de fond
    ->fonction d'affichage d'un objet(ennemi, allie, autre)
A faire:
    ->probleme sur l'image du canvas
    ->gerer positionnement des widgets et le format du labelscore
    ->fonctions Affichage, Deplacement, Supprimer
    ->ajouter fonctions menus
"""
#Librairies
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar
from Jeu import Jeu

#Fonctions
def fScore(Totpts, Newpts):
    '''Permet d'afficher en temps reel le score du joueur'''
    global score
    Totpts += Newpts
    score.set('Score actuel: ' + str(Totpts))

def fNewGame():
    '''Fonction active du bouton new game. Creer une instance de jeu grace a la classe jeu.'''
    mg = Jeu(mv)

def fAffichage():
    '''Affiche un objet (ennemi, allie, protection, tir) à la position indiqué'''

def fDeplacement():
    '''Deplace un objet de la variation indique'''

def fSupprimer():
    '''Supprime du canvas l'objet designe'''

#Fenetre
#Creation et configuration de la fenetre
mv = Tk()
mv.title('Compan and Fels: Space Invaders')
mv.geometry('612x700')

#Creation et configuration des Labels
score = StringVar()
LabelScore = Label(mv, textvariable = score, borderwidth = 1, relief = 'raised')

#Creation et configuration des boutons
ButtonQuit = Button(mv, text = "QUITTER", command = mv.destroy)
ButtonNewGame = Button(mv, text = "NEW GAME", command = fNewGame())

#Creation et configuration du menu
MenuBar = Menu(mv)
MenuFichier = Menu(MenuBar, tearoff = 0)
MenuPropos = Menu(MenuBar, tearoff = 0)
MenuBar.add_cascade(label = 'Fichier', menu = MenuFichier)
MenuBar.add_cascade(label = 'A propos', menu = MenuPropos)
MenuFichier.add_command(label = 'Quitter', command = mv.destroy)
MenuPropos.add_command(label = 'Regles du jeu')
MenuPropos.add_command(label = 'Sur nous')
mv.config(menu = MenuBar)

#Creation et configuration du Canvas
GameZone = Canvas(mv, height = 612, width = 612, background='black')
#background = PhotoImage(master = 'GameZone' ,file = 'image/BgBonbon.png')
#GameZone.create_image(0, 0, image = background)
#GameZone.image(background)

#Positionnement
GameZone.pack(side = "bottom")
ButtonNewGame.pack(side = "left", pady = 10)
ButtonQuit.pack(side = "left", pady = 10)
LabelScore.pack(side = 'left')
