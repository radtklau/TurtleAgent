from turtle import Turtle
import random


class TurtleAgent(Turtle):
    def __init__(self):
        super().__init__()
        self.energy = random.randint(0,100) #born with random energy, if energy reaches zero turtle dies
        self.vision = (random.randint(0,10), random.randint(0,180)) #(vision distance, field of sight)
        self.velo = random.randint(0,10) #distance a turtle can cover in one time step
        self.dead = False

        self.speed(0)
        self.color("green")
        self.penup()

    def eat(self, food):
        self.energy += food.energy

    def move(self):
        self.energy -= 1

    def die(self):
        if self.energy <= 0:
            self.dead = True

    