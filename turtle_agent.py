from turtle import Turtle
import random

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)

turtles = []
for _ in range(100):
    turtle = Turtle()
    turtle.color("green")
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -250)  # Set initial position to (0, 0)
    turtle.setheading(90)
    turtles.append(turtle)

for i in range(100):
    for turtle in turtles:
        turtle.setheading(random.randint(0,180))
        turtle.pendown()
        #turtle.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        #turtle.width(random.choice([1,5,10,20]))
        turtle.forward(random.randint(0,100))

screen.update()
screen.mainloop()

class TurtleAgent(Turtle):
    def __init__(self):
        super().__init__()
        self.energy = random.randint(0,100)

        self.speed(0)
        self.color("green")
        self.penup()