#from turtle import Turtle, TurtleScreen
from environment import Environment
from turtle_agent import TurtleAgent
import json

def append_data(data_dict, new_data):
    # Increment the key to the next available number
    next_key = str(len(data_dict) + 1)
    data_dict[next_key] = new_data

if __name__=="__main__":
    env = Environment()
    env.screen.setworldcoordinates(0,0,1000,1000)
    env.screen.mode("world")
    env.screen.colormode(255)
    env.spawn_food()
    env.spawn_turtles()
    
    turtle_histories = []
    break_flag = False

    while True: #BUG breaks to early (not all data is printed)
        for turtle in env.turtles:
            if turtle.dead:
                if turtle.history not in turtle_histories:
                    turtle_histories.append(turtle.history) #capture turtle history
                if len(turtle_histories) == len(env.turtles):
                    break_flag = True
                    break
                continue
            else:
                food_obj = turtle.look(env.food)
                turtle.move(food_obj)
                
        if break_flag:
            break
        
        
    file_path = 'data/training_0.json'
    data_dict = {}
    
    try:
        with open(file_path, 'r') as json_file:
            data_dict = json.load(json_file)
    except FileNotFoundError:
        # The file doesn't exist, so we catch the `FileNotFoundError` exception and initialize an empty dictionary.
        pass

    new_data = turtle_histories[-1]
    append_data(data_dict, new_data)

    with open(file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
        

        

    