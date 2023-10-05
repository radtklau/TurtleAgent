import turtle
from turtle_agent import TurtleAgent

# Create a custom environment class
class Environment:
    def __init__(self):
        # Create a Screen object
        self.screen = turtle.Screen()
        self.screen.bgcolor("white")  # Set background color
        self.screen.setup(500, 500, 0, 0)

    def create_turtle(self):
        # Create a Turtle object
        new_turtle = TurtleAgent()
        return new_turtle
