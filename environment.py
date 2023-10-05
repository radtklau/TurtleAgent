from turtle import Turtle, Screen

class Environment(Screen):
    def __init__(self):
        super().__init__(canvas=None)
        self.bgcolor("black")
        self.setup(width=500, height=500, startx=0, starty=0)
        self.food = []
