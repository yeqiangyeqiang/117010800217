import turtle, datetime
def drawGap(): 
    turtle.penup()
    turtle.fd(5)
    
def drawLine(draw):   
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
    
def drawDigit(d): 
    turtle.pencolor("red")
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    turtle.pencolor("orange")
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    turtle.pencolor("yellow")
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    turtle.pencolor("green")
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.pencolor("black")
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    turtle.pencolor("blue")
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    turtle.pencolor("purple")
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
    
def drawDate(date):
    for i in date:
            drawDigit(eval(i))
            
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate('88888888')
    turtle.hideturtle()
main()
