from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DIST_START = 5  # initial move distance
SPEED_INCREMENT = 5  # move distance increase per level up


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DIST_START

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            random_y = random.randint(-240, 240)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += SPEED_INCREMENT
