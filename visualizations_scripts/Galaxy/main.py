import turtle

t = turtle.Turtle()
s = turtle.Screen()

color = ['orange','red','magenta','blue','magenta','yellow','green','yellow','green','cyan','purple']

s.bgcolor("black")
t.pensize(2)
t.speed(0)

for x in range (360):
    t.pencolor(color[x%len(color)])
    t.width(x//100 + 1)
    t.forward(x)
    t.right(88) # 59

turtle.hideturtle()
turtle.done()