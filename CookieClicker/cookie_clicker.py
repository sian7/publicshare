# Cookie Clicker
# Simple Cookie Clicker Clone
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible

#import de turtle pour la fenetre et le crayon du jeu 
import turtle

#import de sleep pour les pause
from time import sleep

#je crée la fenetre avec turtle 
screen = turtle.Screen()
#je met le titre et la couleur de font
screen.title("Cookie Clicker")
screen.bgcolor("black")

#variables
#tuples info text :  font + position
_infoFont=("Arial",8,"normal")
_infoPosition=(0,200)
#tuples notice text :  font + position
_noticePosition=(0,220)
_noticeFont=("Serif",10,"bold")
#tuple pour l'animation
_animPosition=(0,-260)
_animFont=("Serif",16,"bold")
_animDelay=1
#text
_textAlign="center"
_textColor="white"
#clicks
clicks = 0

#j'enregistre et je met l'image de cookie
screen.register_shape("cookie.gif")
cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

#j'écrie le text qui affiche les click
pen = turtle.Turtle()
pen.hideturtle()
pen.color(_textColor)
pen.penup()
pen.goto(_infoPosition)
pen.write(arg=f"Clicks: {clicks}",align=_textAlign, font=_infoFont)

#je définie la méthode que j'effectue au click
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(arg=f"Clicks: {clicks}",align=_textAlign,font=_infoFont)
    noticeGamer()
    pen.goto(_infoPosition)

#je définie la méthode qui informe le joueur 
def noticeGamer():
    global clicks
    pen.goto(_noticePosition)
    #tous les 10 click j'informe le joueur
    if (clicks%10==0) :
        pen.write(arg=f"deja {clicks} clicks",align=_textAlign,font=_noticeFont)
    if (clicks==30) : 
        cookie.onclick(nothing)
        anim(clicks)
        #cookie.onclick(clicked)
    
 

#je définie anim
def anim(steps):
    header=f'''
|__   __   __        __  
|__) |  ' (__( (__| (__) 
                                {steps}
                                    '''


    delay=_animDelay/steps
    #header = "bravo"
    i=0
    pen.goto(_animPosition)
    while i<steps :
        #efface 
        pen.clear()
        #ecrir
        pen.write(header,align=_textAlign,font=_animFont)
        #attend
        sleep(delay)
        #efface
        pen.clear()
        #ecrir
        pen.write(header,align=_textAlign,font=_animFont)
        #attend
        sleep(delay)
        #effacer
        pen.clear()
        #pen.write(arg=f"{i}",align=_textAlign,font=_noticeFont)
        i=i+1 
    
def nothing():
    clicks=0


#j'utilise ma méthode (clicked) lorsque le cookie est cliqué 
cookie.onclick(clicked)

#je lance la boucle principal du jeu
screen.mainloop()