from turtle import Turtle
import random
import math

class TurtleAgent(Turtle):
    def __init__(self, plant):
        super().__init__()
        self.plant = plant #if True, turtle is only an non active plant that can be eaten as food
        self.penup()
        self.speed(0)
        #self.colormode(255)

        if not self.plant:
            self.energy = random.randint(0,100) #born with random energy, if energy reaches zero turtle dies
            self.vision = (random.randint(0,100), random.randint(0,180)) #(vision distance, field of sight)
            self.velo = random.randint(0, self.vision[0]) #distance a turtle can cover in one time step (not greater than vision dist)
            self.setposition(500,500)
            self.dead = False
            self.c = [0,255,0]
            self.color(tuple(self.c))
            self.energy_cons = random.uniform(0.25,10.0)
        else:
            self.energy = random.randint(5,25) #how much energy the plant contains
            self.position = ((random.randint(0,1000), random.randint(0,1000)))
            self.setposition(self.position)
            self.hideturtle()
            self.color("blue")
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
        r = int(255*(1-self.energy/100))
        g = int(255 * self.energy/100)
        b = 0
        if r > 255:
            r = 255
        if r < 0:
            r = 0
        if g > 255:
            g = 255
        if g < 0:
            g = 0
        self.c = [r, g, b]
        self.color(tuple(self.c))
        self.energy -= self.energy_cons
        if target:
            self.goto(target.pos())
            self.eat(target)
        else:
            while True:
                self.setheading(random.randint(0,360))
                self.forward(self.velo)
                if self.pos()[0] < 0 or self.pos()[1] < 0 or self.pos()[0] > 1000 or self.pos()[1] > 1000:
                    self.undo()
                else:
                    break
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


            

                

    