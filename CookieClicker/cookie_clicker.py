# Cookie Clicker
# Simple Cookie Clicker Clone
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @Fenix and @Sian
import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker by @Fenix")
wn.bgcolor("black")

#"TEXT"
#"(fontname, fontsize, fonttype)"
_fontInfo=("Arial",8,"normal")
_fontNotice=("Serif",10,"bold")
_textAlign="center"
_textPosition=(0,200)
_noticePosition=(0,220)
_textColor="white"

wn.register_shape("cookie.gif")

cookie = turtle.Turtle()
cookie.shape("cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color(_textColor)
pen.penup()
pen.goto(_textPosition)
pen.write(arg=f"Clicks: {clicks}",align=_textAlign, font=_fontInfo)

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    #pen.write(arg=f"Clicks: {clicks}", align=_textAlign, font=_font)"
    pen.write(arg=f"Clicks: {clicks}",align=_textAlign,font=_fontInfo)
    noticed()
    pen.goto(_textPosition)


def noticed():
    global clicks
    pen.goto(_noticePosition)
    if (clicks%10==0) :
        pen.write(arg=f"deja {clicks} clicks",align=_textAlign,font=_fontNotice)
    
cookie.onclick(clicked)

wn.mainloop()