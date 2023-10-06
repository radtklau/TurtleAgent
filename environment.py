import turtle
from turtle_agent import TurtleAgent
import random

# Create a custom environment class
class Environment:
    def __init__(self):
        # Create a Screen object
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")  # Set background color
        self.food = []
        self.turtles = []

    def spawn_turtles(self):
        # Create a Turtle object
        for _ in range(25):
            new_turtle = TurtleAgent(plant=False)
            self.turtles.append(new_turtle)
    
    def spawn_food(self):
        for _ in range(50):
            new_plant = TurtleAgent(plant=True)
            self.food.append(new_plant)
