# Cookie Clicker
# Simple Cookie Clicker Clone using turtle
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible

#import de turtle pour la fenetre et le crayon du jeu 
import turtle

#import de sleep pour les pause
from time import sleep

#variables

#tuples info text :  Police + position
_infoFont=("Arial",8,"normal")
_infoPosition=(0,200)
#tuples notice text :  Police + position
_noticePosition=(0,220)
_noticeFont=("Serif",10,"bold")
#tuples pour l'animation
_animPosition=(0,-260)
_animFont=("Serif",16,"bold")
#tuples pour les tours
_tourPosition=(0,240)
_tourFont=("Serif",14,"bold")

#text
_textAlign="center"
_textColor="white"


#clicks
clicks = 0
tours=0

#parametre
noticedClick=5
goal=6
maxTours=5
_animDelay=1


#Mes méthode

#je définie la méthode qui informe le joueur 
def noticeGamer():
    global clicks
    pen.penup()
    pen.goto(_noticePosition)
    #tous les 10 click j'informe le joueur
    if (clicks%noticedClick==0) :
        pen.write(arg=f"deja {clicks} clicks",align=_textAlign,font=_noticeFont)

    if (clicks==goal) : 
        anim(clicks)
        if (tours==maxTours) : exit(0)
        drawcookie()

def drawTour():
    global tours   
    if tours>0 :
        pen.penup()
        pen.goto(_tourPosition)
        pen.write(arg=f"{tours}",font=_tourFont)

def drawcookie():
    name=f"cookie{tours}.gif"
    global screen 
    screen.register_shape(name)
    global cookie
    cookie.shape(name)

#je définie anim
def anim(steps):
    #je compte les tour
    global tours
    tours=tours+1
    #je récupere les clicks je le set a 0
    global clicks
    clicks=0
    #j'assigne bravo 
    bravo=f'''
    |__   __   __        __  
    |__) |  ' (__( (__| (__) 
                                    {steps}
                                        '''
    #délai de clignotement
    delay=(_animDelay/steps)/2
    i=0
    pen.penup()
    pen.goto(_animPosition)
    #boucle qui me sert a faire clignoter bravo
    while i<steps :
        #efface 
        pen.clear()
        #ecrir
        pen.write(bravo,align=_textAlign,font=_animFont)
        #attend
        sleep(delay)
        #efface
        pen.clear()
        #ecrir
        pen.write(bravo,align=_textAlign,font=_animFont)
        #attend
        sleep(delay)
        #effacer
        pen.clear()
        #j'incrémente i pour sortir de la boucle quand i = steps
        i=i+1 
    #pause pour éviter des bug d'affichage  
    sleep(_animDelay)
    pen.write("GO",align=_textAlign,font=_animFont)   

#je définie la méthode que j'effectue au click
def clicked(x, y):
    
    global cookie
    global clicks
    global tours
    
    cookie.onclick(None) 
    clicks += 1

    pen.clear()
    pen.penup()
    pen.goto(_infoPosition)
    pen.write(arg=f"Clicks: {clicks}",align=_textAlign,font=_infoFont)

    drawTour()
    
    noticeGamer()

    cookie.onclick(clicked)
    
#je crée la fenetre avec turtle 
screen = turtle.Screen()
#je met le titre et la couleur de font
screen.title("Cookie Clicker")
screen.bgcolor("black")

#j'enregistre et je met l'image de cookie
cookie = turtle.Turtle()
drawcookie()
cookie.speed(0)

#j'écrie le text qui affiche les click
pen = turtle.Turtle()
pen.hideturtle()
pen.color(_textColor)
pen.penup()
pen.goto(_infoPosition)
pen.write(arg=f"Clicks: {clicks}",align=_textAlign, font=_infoFont)

#j'utilise ma méthode (clicked) lorsque le cookie est cliqué 
cookie.onclick(clicked)

#je lance la boucle principal du jeu
screen.mainloop()