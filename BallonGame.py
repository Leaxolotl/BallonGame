from tkinter import *
from random import *

class Application :
    def __init__(self) :
        self.fenetre = Tk() # Création d'une fenêtre graphique
        self.fenetre.title("Tir aux ballons") # Titre de la fenêtre
        self.fenetre.geometry("800x620") # dimension de la fenêtre
        self.zone_graphique =  Canvas(self.fenetre , width = 600 , height = 600 , bg = "#0099AA") # On déclare une zone graphique dans la fenêtre
        self.zone_graphique.place(x = 10, y = 10) # On place la zone graphique en utilisant les coordonnées
        self.bg = PhotoImage(file = "ciel.png")
        self.label = Label(self.fenetre,text = "Score : ")
        self.label.place(x = 650, y = 100)
        self.score = 0
        self.zone_graphique.create_image(0 , 0 , image = self.bg , anchor="nw")
        self.bouton1 = Button(self.fenetre, text = "Quitter", width = 10, command = quit)
        self.bouton1.place(x = 650 , y = 190)
        self.bouton2 = Button(self.fenetre, text = "Jouer", width = 10, command = self.jouer)
        self.bouton2.place(x = 650 , y = 150)
        
    def quit() :
        fenetre.destroy()
        
    def jouer(self):
        self.zone_graphique.delete("all")
        self.bg = PhotoImage(file = "ciel.png")
        self.zone_graphique.create_image(0 , 0 , image = self.bg , anchor="nw")
        self.score = 0
        ballons = []
        debut()
    
        
class Ballon :
    def __init__(self, jeu) :
        self.x = randint(100,500)
        self.y = randint(550,1000)
        self.dx = 0
        self.dy = 2
        self.jeu = jeu 
        self.bal_ima = PhotoImage(file = "ballon" + str(randint(0,5)) + ".png")
        self.num_ima = jeu.zone_graphique.create_image(self.x , self.y , image = self.bal_ima , anchor="nw")
        self.mouvement()
        
    def mouvement(self) :
        self.y = self.y - self.dy
        if self.y < -50 :
            self.y = 650
        self.jeu.zone_graphique.coords(self.num_ima, self.x, self.y)
        self.jeu.zone_graphique.after(20, self.mouvement)
        
        
class Viseur :
    def __init__(self, jeu, ballons) :
        self.x = 0
        self.y = 0
        self.ballons = ballons
        self.jeu = jeu 
        self.souris_ima =  PhotoImage(file = "viseur.png")
        self.num_ima_viseur = self.jeu.zone_graphique.create_image(self.x, self.y, image = self.souris_ima, anchor = "center")
        self.jeu.zone_graphique.bind("<Motion>", self.move)
        self.jeu.zone_graphique.bind("<Button-1>", self.destroy)
         
    def move(self, event) :
        self.jeu.zone_graphique.coords(self.num_ima_viseur, event.x, event.y)  
        
    def destroy(self, event) :
        for i in range(len(self.ballons)-1,-1,-1):
            if self.ballons[i].x <= event.x <= self.ballons[i].x+50 and self.ballons[i].y <= event.y <= self.ballons[i].y+75 :
                self.jeu.zone_graphique.delete(self.ballons[i].num_ima)
                self.jeu.label['text']
                self.jeu.score += 1
                self.jeu.label['text'] = "Score : " + str(self.jeu.score)
                del self.ballons[i]
                break
        
       
jeu = Application()

def debut():
    ballons = []
    for i in range(40):
        ballons.append(Ballon(jeu))
    viseur = Viseur(jeu, ballons)
    
mainloop()