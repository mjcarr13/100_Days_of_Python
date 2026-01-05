from turtle import Turtle
import random


class Car():
    def __init__(self):
        self.all_cars = []
        self.make_cars()
        self.spread_cars()

    def make_cars(self):
        num_cars = random.randint(15,35)
        for _ in range(num_cars):
            car = Turtle(shape="square")
            car.penup()
            car.setheading(180)
            car.shape("square")
            car.shapesize(1, 3)
            rand_color = random.choice(["green", "red", "yellow", "blue", "pink", "purple"])
            car.color(rand_color)
            self.all_cars.append(car)

    def spread_cars(self):
        for index, car in enumerate(self.all_cars):
            # rand_size = random.randint(2,5)
            # car.shapesize(1, rand_size)
            starting_y = round(random.randint(-250, 270), -1)
            starting_x = round(random.randint(100, 1500), -1)
            car.goto(x=starting_x, y=starting_y)
            if car.ycor() == self.all_cars[index-1].ycor() or car.xcor() == self.all_cars[index-1].xcor():
                starting_y = round(random.randint(-250, 270), -1)
                starting_x = round(random.randint(100, 1500), -1)
                car.goto(x=starting_x, y=starting_y)


    def cars_move(self):
        for i in range(len(self.all_cars)):
            new_x = self.all_cars[i].xcor() - 10
            self.all_cars[i].goto(new_x,self.all_cars[i].ycor())
            if self.all_cars[i].xcor() <= -330:
                reset_colour = random.choice(["green", "red", "yellow", "blue", "pink", "purple"])
                self.all_cars[i].color(reset_colour)
                reset_y = round(random.randint(-270, 270), -1)
                reset_x = random.randint(320, 2000)
                self.all_cars[i].goto(x=reset_x, y=reset_y)

    def refresh(self):
        for car in self.all_cars:
            reset_colour = random.choice(["green", "red", "yellow", "blue", "pink", "purple"])
            car.color(reset_colour)
            self.spread_cars()








