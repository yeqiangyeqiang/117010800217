import turtle as t
t.penup()
t.fd(-120)
t.pendown()
t.pensize(21)
t.pencolor("red")
t.seth(-40)
for i in range(3):
    t.circle(40,80)
    t.penup()
    t.pendown()
    t.pencolor("purple")
    t.circle(-40,80)
    t.penup()
    t.pendown()
    t.pencolor("blue")
t.circle(40,80/2)
t.fd(60)
t.penup()
t.pendown()
t.pencolor("yellow")
t.circle(20,140)
t.fd(40*2/3)    
t.circle(100,60)
t.pencolor("green")
t.circle(20,140)
t.fd(40*2/3)    
