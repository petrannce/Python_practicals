import turtle

t = turtle.Turtle()
t.speed(10)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

turtle.bgcolor('black')
for i in range(360):
    t.color(colors[i % 7])
    t.circle(100)
    t.right(10)
turtle.done()
