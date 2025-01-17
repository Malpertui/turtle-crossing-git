import time
from turtle import Screen
from player import Player
from car_manager2 import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

screen.listen()

scoreboard = Scoreboard()

all_cars = []
car = CarManager()
car1 = CarManager()
car2 = CarManager()
car3 = CarManager()
car4 = CarManager()
car5 = CarManager()
car6 = CarManager()
car7 = CarManager()
car8 = CarManager()
car9 = CarManager()
car10 = CarManager()
car11 = CarManager()

all_cars.append(car)
all_cars.append(car1)
all_cars.append(car2)
all_cars.append(car3)
all_cars.append(car4)
all_cars.append(car5)
all_cars.append(car6)
all_cars.append(car7)
all_cars.append(car8)
all_cars.append(car9)
all_cars.append(car10)
all_cars.append(car11)

player = Player()
screen.onkeypress(player.go_up, "Up")

while game_is_on:
    screen.update()

    for one_car in all_cars:
        one_car.move()
        if one_car.xcor() < -320:
            one_car.reset_position()

    for this_car in all_cars:
        if player.distance(this_car) < 40:
            scoreboard.game_over()
            screen.update()
            time.sleep(5)
            game_is_on = False

    if player.ycor() > 290:
        scoreboard.score_update()
        player.reset_position()
        for that_car in all_cars:
            that_car.increase_speed()

screen.exitonclick()



