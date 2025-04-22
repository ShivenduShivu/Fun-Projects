import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.width(1)
t.speed(15)
col = ['green','white','red','yellow']
for i in range(100):
    t.pencolor(col[i % 4])
    t.forward(i * 3)
    t.left(125)
    t.right(30)
    t.left(137)
    t.right(30)
    t.left(30)
    t.right(120)
turtle.done()
