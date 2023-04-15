from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.lt(180)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DISTANCE)

    def new_level(self):
        new_speed = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        # try to think of how to make move_car function take in a variable input
        for car in self.all_cars:
            car.fd(new_speed)
