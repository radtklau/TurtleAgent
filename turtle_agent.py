from turtle import Turtle
import random
import math

class TurtleAgent(Turtle):
    def __init__(self, plant):
        super().__init__()
        self.plant = plant #if True, turtle is only an non active plant that can be eaten as food
        self.penup()
        self.speed(0)

        if not self.plant:
            self.energy = random.randint(0,100) #born with random energy, if energy reaches zero turtle dies
            self.vision = (random.randint(0,100), random.randint(0,180)) #(vision distance, field of sight)
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
            self.eaten = False
            self.pendown()
            self.dot(5)
            self.penup()

    def eat(self, food):
        self.energy += food.energy
        food.eaten = True
        food.color("black")
        food.pendown()
        food.dot(5)

    def move(self, target=None):
        self.energy -= 1
        if target:
            self.goto(target.pos())
            self.eat(target)
        else:
            self.setheading(random.randint(0,360))
            self.forward(self.velo)
        if self.energy <= 0:
            self.die()
        #self.show_fov()

    def die(self):
        self.dead = True

    def look(self, food_objects): #check whether turtle can see any food from list food_objects with all food objects
        for food in food_objects:
            food_pos = food.pos()
            turtle_pos = self.pos()
            dist = ((food_pos[0] - turtle_pos[0]) ** 2 + (food_pos[1] - turtle_pos[1]) ** 2) ** 0.5

            if dist <= self.vision[0] and not food.eaten:
                return food  # Food is within the field of view
            else:
                continue

        return None  # Food is not within the field of view
            
    def show_fov(self):
        self.clear()
        self.pendown()
        self.circle(self.vision[0])
        self.penup()


            

                

    