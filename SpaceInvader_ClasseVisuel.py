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
    methode gestion de tour ( avec un pb sur les collisions);
A faire: Voir si on modifie l'apparence des boutons;
    reflechir a differentes ameliorations possibles;
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
        self.labelBestScore.pack(side = 'top')                       #Amener a changer en fonction du rendu

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
        self.fResetVisuel()
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
            self.bestscore.set('Best score: ' + str(self.valeurbestscore))

    def fResetVisuel(self):
        '''Reset le visuel'''
        #Creation des labels de score
        self.valeurscore = 0
        self.fScore()

        #Creation d'une liste des entitees affichee
        self.entityId = []

        #Apparition du joueur sur le Canvas GameZone
        self.fAffichage(self.mg.joueur)

        #Apparition des blocs de protections
        self.fAffichageBlocs()

        #Apparition des ennemis sur le Canvas
        self.fAffichageVague()
        
        #Augmentation du nombre de tour jouer par 100ms (c'est pas fun de reset en boucle donc ça augmente le nombre de tour qui se joue)
        self.fGestionTour()
    
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
            self.mg.fDeplacement(objet, direction, sens)
            if objet.position[direction] < 10:
                objet.position[direction] = 10
                self.GameZone.move(objet.id, - sens * objet.vitesse[direction], 0)
            elif 602 < objet. position[direction] + objet.hitbox[direction]:
                objet.position[direction] = 602 - objet.hitbox[direction]
                self.GameZone.move(objet.id, - sens * objet.vitesse[direction], 0)
        else:
            self.GameZone.move(objet.id, 0, sens * objet.vitesse[direction])
            self.mg.fDeplacement(objet, direction, sens)
            if objet.position[direction] < 10:
                objet.position[direction] = 10
                self.GameZone.move(objet.id, 0, - sens * objet.vitesse[direction])
            elif 602 < objet. position[direction] + objet.hitbox[direction]:
                objet.position[direction] = 602
                self.GameZone.move(objet.id, 0, - sens * objet.vitesse[direction])
            if objet.type == -1 and objet.position[direction] in [10, 602]:
                objet.vie -= 1
    
    def fSupprimer(self, objet):
        '''Supprime l'objet de l'écran si sa vie tombe a 0'''
        self.mg.fSuppression(objet)
        if objet.vie <= 0:
            self.entityId.remove(objet.id)
            self.GameZone.delete(objet.id)
    
    #Methodes avances propre au Canvas GameZone
    def fMoveEnnemi(self):
        '''Deplace tous les ennemis sur le Canvas GameZone selon une direction et un sens precis.
        -1 a gauche, 0 en bas, 1 a droite'''
        if self.mg.ennemidir == 1:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, 1)
            if self.mg.ennemirepere.position[0] + self.mg.ennemirepere.hitbox[0] == 602:
                self.mg.ennemidir = -1
        elif self.mg.ennemidir == -1:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 0, -1)
            if self.mg.ennemirepere.position[0] == 10:
                if self.mg.ennemirepere.position[1] + self.mg.ennemirepere.hitbox[1] == 602:
                    self.mg.ennemidir = 1
                else:
                    self.mg.ennemidir = 0
        elif self.mg.ennemidir == 0:
            for entity in self.mg.ennemis:
                self.fDeplace(entity, 1, 1)
            self.mg.ennemidir = 1
    
    def fMoveEnnemiSpeciaux(self):
        '''Deplace tous les ennemis speciaux sur le Canvas GameZone selon une direction et un sens precis.
        -1 a gauche, 1 a droite et suppr si 0'''
        if self.mg.ennemisspeciaux != [] and self.mg.ennemisspeciauxdir == 1:
            for entity in self.mg.ennemisspeciaux:
                self.fDeplace(entity, 0, 1)
            if self.mg.ennemisspeciaux[0].position[0] + self.mg.ennemisspeciaux[0].hitbox[0] == 602:
                self.mg.ennemisspeciauxdir = -1
        elif self.mg.ennemisspeciaux != [] and self.mg.ennemisspeciauxdir == -1:
            for entity in self.mg.ennemisspeciaux:
                self.fDeplace(entity, 0, -1)
            if self.mg.ennemirepere.position[0] == 10:
                self.mg.ennemisspeciauxdir = 1
                self.GameZone.delete(self.mg.ennemisspeciaux[0].id)
                self.mg.entity.remove(self.mg.ennemisspeciaux[0])
                self.mg.ennemisspeciaux.remove(self.mg.ennemisspeciaux[0])
                

    def fMoveTir(self):
        '''Deplace tous les tir sur le Canvas GameZone sur l'axe y et dans le sens precise dans leur vitesse'''
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
        if self.mg.ennemisspeciaux == [] and randint(0,100) == 42:
            self.mg.fCreationEnnemiSpecial()
            self.fAffichage(self.mg.ennemisspeciaux[0])
    
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
            #self.mg.fTirPossible()
            self.mg.fCreation(-1, 1, 0, [self.mg.joueur.position[0] + 13, self.mg.joueur.position[1] - 6], (5, 5), [0, -10])
            self.fAffichage(self.mg.tirs[-1])
            #self.mv.after(2000, self.mg.fTirPossible())
        elif action == 'Return':
            if self.mg.run == True:
                self.mg.run == False
            else:
                self.mg.run = True

    #Methode gestion du tour
    def fGestionTour(self):
        '''Gere le deroulement d'un tour, puis apres un certain temps se reactive.'''
        if self.mg.gameover == False:
            if self.mg.run == True:
                self.fAffichageEnnemiSpeciaux()
                self.mg.fTrouverRepere()
                self.fMoveEnnemiSpeciaux()
                self.fMoveEnnemi()
                self.fMoveTir()
                self.mg.fCollision(self.mg.joueur)         
                for entity in self.mg.entity:
                        self.mg.fCollision(entity)
                        self.fSupprimer(entity)
                self.fScore()
                self.fBestScore()
                self.mg.fGameOver()
                if self.mg.ennemis == []:
                    self.mg.fCreationVague()
                    self.fAffichageVague()
        self.mv.after(100, self.fGestionTour)
    