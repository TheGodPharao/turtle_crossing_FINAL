import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
car_manager = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(tim.move_turtle, "Up")

game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision with cars and GAME OVER SEQUENCE
    for car in car_manager.all_cars:
        if tim.distance(car) < 20:
            game_is_on = False
            level.game_over()

    # detect successful finish
    if tim.is_at_finish_line():
        tim.reset_position()
        car_manager.new_level()
        level.new_level()


screen.exitonclick()
