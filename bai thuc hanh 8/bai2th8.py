from bai1th8 import painter
print("DINH VAN VIET MSV:235752021610067")
import turtle, random
colors =["red","green","blue","orange","purple","pink","yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)
    painter.pencolor(colors)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
