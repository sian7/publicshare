# Cookie Clicker
# Simple Cookie Clicker Clone
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible

#import de turtle pour la fenetre et le crayon du jeu 
import turtle

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
    if (clicks==20) : anim(clicks)

#je définie anim
def anim(steps):
    i=0
    pen.goto(-50,-200)
    while i<steps :
        pen.write(arg=f"{i}",align=_textAlign,font=_noticeFont)
        #faire une pause
        
        #effacer

        i=i+1 
    pen.write("bravo")


#j'utilise ma méthode (clicked) lorsque le cookie est cliqué 
cookie.onclick(clicked)

#je lance la boucle principal du jeu
screen.mainloop()