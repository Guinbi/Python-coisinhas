from math import *
import turtle as tur

tur.speed(0)
x = 0
y = 0
siz = int(input("Diga o tamanho do cubo: "))

def pos(x, y, pen):
    if pen == False:
        tur.penup()
    if pen == True:
        tur.pendown()

    tur.setpos(x, y)
    tur.pendown()
    
def drawCube(size):
        def drawRect(dir):
            if dir == "fr":
                tur.fd(size)
                tur.right(90)
                tur.fd(size)
                tur.right(90)
                tur.fd(size)
                tur.right(90)
                tur.fd(size)
            if dir == "tr":
                tur.bk(size)
                tur.right(90)
                tur.fd(size)
                tur.left(90)
                tur.fd(size)
                tur.left(90)
                tur.fd(size)
        
        drawRect("fr")
        pos(size / 2 + x, -size / 2 + y, False)
        tur.penup()
        tur.seth(45)
        tur.forward(size * 1.4)
        tur.seth(0)
        tur.pendown()
        drawRect("tr")
        tur.seth(-135)
        tur.forward(size / 2 * 1.4)
        tur.seth(180)
        tur.forward(size)
        tur.seth(45)
        tur.forward(size / 2 * 1.4)
        tur.seth(0)
        tur.forward(size)
        tur.seth(270)
        tur.forward(size)
        tur.seth(-135)
        tur.forward(size / 2 * 1.4)
        tur.seth(180)
        tur.fd(size)
        tur.seth(45)
        tur.fd(size / 2 * 1.4)

pos(x, y, False)
drawCube(siz)

input()