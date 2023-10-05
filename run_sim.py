#from turtle import Turtle, TurtleScreen
from environment import Environment
from turtle_agent import TurtleAgent

if __name__=="__main__":
    env = Environment()
    env.screen.setworldcoordinates(0,0,1000,1000)
    env.screen.mode("world")
    env.spawn_food()
    env.spawn_turtles()

    while True:
        for turtle in env.turtles:
            if turtle.dead:
                continue
            turtle.move()

