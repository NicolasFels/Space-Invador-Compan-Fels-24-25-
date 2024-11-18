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
    ->ajouter fonctions menus (remplir texte et recommencer pour a propos)
"""
#Librairies
from tkinter import Tk, Canvas, Button, PhotoImage, Menu, Label, StringVar, Toplevel, LabelFrame, Frame
# from PIL import ImageTk, Image
# from Classe_Jeu import Jeu

#Fonctions
def fScore(Totpts : int, Newpts : int):
    '''Permet d'afficher en temps reel le score du joueur'''
    global score
    Totpts += Newpts
    score.set('Score actuel: ' + str(Totpts))

#def fNewGame(visuel):
#    '''Fonction active du bouton new game. Creer une instance de jeu grace a la classe jeu.'''
#    mg = Jeu(visuel)

def fAffichage(entity):
    '''Affiche l'objet spatial sur le canvas -1 0 1'''
    if entity.type == -1:
        couleur = 'rouge'
    elif entity.type == 0:
        couleur = 'blanc'
    elif entity.type == 1:
        couleur = 'bleu'
    entity.forme = GameZone.create_rectangle(entity.position[0], entity.position[1], entity.position[0] + entity.taille[0], entity.postion[1] + entity.taille[1])

def fDeplace(entity):
    '''Deplace un objet de la variation indiquee'''
    GameZone.move(entity.forme, entity.vitesse[0], entity.vitesse[1])

def fSupprimer(entity):
    '''Supprime du canvas l'objet designe'''
    GameZone.destroy(entity.forme)

def create(): 
    # Creation des fenetres du menu
    regle = Toplevel(mv)
    regle.title('Regles du jeu')
    TitreRegle = LabelFrame(regle, text = "Regles du jeu", padx = 20, pady = 20)
    TitreRegle.pack(fill = 'both', expand = 'yes')
    Label(TitreRegle, text = "test").pack()
    
#Fenetre
#Creation et configuration de la fenetre
mv = Tk()
mv.title('Compan and Fels: Space Invaders')
mv.geometry('612x700')

#Creation et configuration des Labels
score = StringVar()
fScore(0, 0)   #A suppr pour vrai fctionnement
LabelScore = Label(mv, textvariable = score)

#Creation et configuration des boutons
ButtonQuit = Button(mv, text = "QUITTER", command = mv.destroy)
ButtonNewGame = Button(mv, text = "NEW GAME")

#Creation et configuration du menu
MenuBar = Menu(mv)
MenuFichier = Menu(MenuBar, tearoff = 0)
MenuPropos = Menu(MenuBar, tearoff = 0)
MenuBar.add_cascade(label = 'Fichier', menu = MenuFichier)
MenuBar.add_cascade(label = 'A propos', menu = MenuPropos)
MenuFichier.add_command(label = 'Quitter', command = mv.destroy)
MenuPropos.add_command(label = 'Regles du jeu', command = create)
MenuPropos.add_command(label = 'Sur nous')
mv.config(menu = MenuBar)

#Creation et configuration du Canvas
# background = ImageTk.PhotoImage(Image.open('BgBonBon.gif'))
GameZone = Canvas(mv, height = 612, width = 612, background = 'black')
# GameZone.create_image(0, 0, image = background)
# GameZone.Image(background)

#Positionnement
GameZone.pack(side = "bottom")
ButtonNewGame.pack(side = "left", pady = 10, padx = 30)
ButtonQuit.pack(side = "right", pady = 10, padx = 30)
LabelScore.pack(side = 'top', pady =30)

mv.mainloop()