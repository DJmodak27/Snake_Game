from turtle import Turtle
x_pos = 290
y_pos = 290

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()


    def move(self):
        self.goto(-x_pos, -y_pos)
        self.pendown()
        self.setpos(x_pos,-y_pos)
        self.setpos(x_pos,y_pos)
        self.setpos(-x_pos, y_pos)
        self.setpos(-x_pos,-y_pos)