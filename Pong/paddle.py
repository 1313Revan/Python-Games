from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 230:
            new_pos = self.ycor() + 20
            self.sety(new_pos)

    def go_down(self):
        if self.ycor() > -230:
            new_pos = self.ycor() - 20
            self.sety(new_pos)
