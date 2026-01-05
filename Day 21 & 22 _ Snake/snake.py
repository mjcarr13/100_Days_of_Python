from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.turtlesize(1, 1)
            segment.goto(position)
            self.segments.append(segment)


    def move_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.turtlesize(1, 1)
        #if snake is facing up, position is last segment minus 20 on y axis
        if self.head.heading() == UP:
            new_seg_x = self.segments[-1].xcor()
            new_seg_y = self.segments[-1].ycor() - 20
            new_segment.goto(new_seg_x, new_seg_y)
        #if snake is facing down, postion is last segment plus 20 on y axis
        if self.head.heading() == DOWN:
            new_seg_x = self.segments[-1].xcor()
            new_seg_y = self.segments[-1].ycor() + 20
            new_segment.goto(new_seg_x, new_seg_y)
        #if snake is facing right, position is last segment minus 20 on x axis
        if self.head.heading() == RIGHT:
            new_seg_x = self.segments[-1].xcor() -20
            new_seg_y = self.segments[-1].ycor()
            new_segment.goto(new_seg_x, new_seg_y)
        #if snake is facing left, position is last segment plus 20 on x axis
        if self.head.heading() == LEFT:
            new_seg_x = self.segments[-1].xcor() + 20
            new_seg_y = self.segments[-1].ycor()
            new_segment.goto(new_seg_x, new_seg_y)

        self.segments.append(new_segment)



    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)







#we have the snake segments. we want each one to

