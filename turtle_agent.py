from turtle import Turtle
import random


class TurtleAgent(Turtle):
    def __init__(self, plant):
        super().__init__()
        self.plant = plant #if True, turtle is only an non active plant that can be eaten as food
        self.penup()
        self.speed(0)

        if not self.plant:
            self.energy = random.randint(0,100) #born with random energy, if energy reaches zero turtle dies
            self.vision = (random.randint(0,10), random.randint(0,180)) #(vision distance, field of sight)
            self.velo = random.randint(0,50) #distance a turtle can cover in one time step
            self.setposition(500,500)
            self.dead = False
            self.color("white")
        else:
            self.energy = random.randint(1,10) #how much energy the plant contains
            self.position = ((random.randint(0,1000), random.randint(0,1000)))
            self.setposition(self.position)
            self.hideturtle()
            self.color("green")
            self.pendown()
            self.dot(5)

    def eat(self, food):
        self.energy += food.energy

    def move(self):
        self.energy -= 1
        self.setheading(random.randint(0,360))
        self.forward(self.velo)
        self.die()

    def die(self):
        if self.energy <= 0:
            self.dead = True

    