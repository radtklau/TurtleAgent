#from turtle import Turtle, TurtleScreen
from environment import Environment
from turtle_agent import TurtleAgent

if __name__=="__main__":
    env = Environment()

    turtles = []
    for _ in range(10):
        turtle = env.create_turtle()
        turtles.append(turtle)

    while True:
        for turtle in turtles:
            turtle.move()

