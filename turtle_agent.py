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
            self.history = {}
            self.steps = 0 #count how many steps the turtle did
            self.energy = 100 #random.randint(99,100) #born with random energy, if energy reaches zero turtle dies
            self.vision = (50, 20) #(random.randint(50,51), random.randint(0,180)) #(vision distance, field of sight)
            self.velo = 100 #random.randint(self.vision[0] -1, self.vision[0]) #distance a turtle can cover in one time step (not greater than vision dist)
            self.setposition(500,500)
            self.dead = False
            self.c = [0,255,0]
            self.color(tuple(self.c))
            self.energy_cons = 10 #random.uniform(0.25,10.0)
        else:
            self.energy = 10 #random.randint(5,25) #how much energy the plant contains
            self.position = ((random.randint(0,1000), random.randint(0,1000)))
            self.setposition(self.position)
            self.hideturtle()
            self.color("blue")
            self.eaten = False
            self.pendown()
            self.dot(5)
            self.penup()

    def _eat(self, food):
        self.energy += food.energy
        food.eaten = True
        food.color("black")
        food.pendown()
        food.dot(5)

    def move(self, target=None):
        energy_feature = self.energy
        heading_feature = int(self.heading())
        
        r = int(255 * (1-self.energy/100))
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
        energy_label = random.uniform(0.0,1.0) #how far to go in one time step but also how much energy is used LABEL!!
        self.energy -= (self.energy_cons * energy_label) + 0.25 #also resting takes some energy
        if target:
            angle = self._calc_angle(target)
            self._turn_toward_angle(angle)
            #self.right(angle - self.heading())
            self.goto(target.pos())
            self.steps += 1
            self._eat(target)
        else:
            while True:
                heading_label = random.randint(0,360)
                self.setheading(heading_label) #direction LABEL!!
                self.forward(self.velo * energy_label)
                self.steps += 1
                if self.pos()[0] < 0 or self.pos()[1] < 0 or self.pos()[0] > 1000 or self.pos()[1] > 1000:
                    self.undo()
                    self.energy += self.energy_cons * energy_label
                    self.steps -= 1
                else:
                    break
            pos_feature = self.pos()
            self.history[self.steps] = [(energy_feature, heading_feature, pos_feature), (energy_label, heading_label)] #feature, label

        if self.energy <= 0:
            self._die()
            #print(self.steps)
            print(self.history)
            print("\n")

        #self._show_fov()

    def _die(self):
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
            
    def _show_fov(self):
        self.clear()
        self.pendown()
        self.circle(self.vision[0])
        self.undo()
        self.penup()

    def _calc_angle(self, food):
        turtle_pos = self.pos()
        food_pos = food.pos()
        vector_turtle_food = (food_pos[0] - turtle_pos[0], food_pos[1] - turtle_pos[1])
        angle_radians = math.atan2(vector_turtle_food[1], vector_turtle_food[0])
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees
    
    def _turn_toward_angle(self, target_angle_degrees):
        # Get the current heading in degrees
        current_heading = self.heading()

        # Calculate the angle difference between the current heading and the target angle
        angle_difference = target_angle_degrees - current_heading

        # Normalize the angle difference to the range [-180, 180] degrees
        if angle_difference > 180:
            angle_difference -= 360
        elif angle_difference < -180:
            angle_difference += 360

        # Determine whether to turn left or right based on the sign of the angle difference
        if angle_difference > 0:
            self.left(angle_difference)
        else:
            self.right(abs(angle_difference))


            

                

    