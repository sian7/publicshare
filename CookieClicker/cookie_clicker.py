# Cookie Clicker
# Simple Cookie Clicker Clone using turtle
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
#tuples pour l'animation
_animPosition=(0,-260)
_animFont=("Serif",16,"bold")
#tuples pour les tours
_tourPosition=(0,240)
_tourFont=("Serif",14,"bold")

#text
_textAlign="center"
_textColor="white"

_animDelay=1

#clicks
clicks = 0
tours=0
goal=15
noticedClick=10



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

def drawTour():
    global tours   
    if tours>0 :
        pen.penup()
        pen.goto(_tourPosition)
        pen.write(arg=f"{tours}",font=_tourFont)


#je définie anim
def anim(steps):
        
    """   
    global cookie
    cookie.onclick(None)  
    """
   
    global tours
    tours=tours+1
    global clicks
    clicks=0
    header=f'''
    |__   __   __        __  
    |__) |  ' (__( (__| (__) 
                                    {steps}
                                        '''

    delay=(_animDelay/steps)/2
    #header = "bravo"
    i=0
    pen.penup()
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

        i=i+1 
    sleep(_animDelay)
    pen.write("GO",align=_textAlign,font=_animFont)   

    #cookie.onclick(clicked)
    #screen.exitonclick()


#je définie la méthode que j'effectue au click
def clicked(x, y):
    
    global cookie
    cookie.onclick(None) 
 
    global clicks
    global tours
    clicks += 1
    pen.clear()
    pen.penup()
    pen.goto(_infoPosition)
    pen.write(arg=f"Clicks: {clicks}",align=_textAlign,font=_infoFont)

    drawTour()
    noticeGamer()

    cookie.onclick(clicked)
    


#j'utilise ma méthode (clicked) lorsque le cookie est cliqué 
cookie.onclick(clicked)

#je lance la boucle principal du jeu
screen.mainloop()