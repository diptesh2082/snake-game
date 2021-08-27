from turtle import Turtle, position

starting_point=[(0,0),(-20, 0), (-40, 0)]
dis = 20
up = 90
down = 270
right = 0
left = 180

class Snake :

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in starting_point:
            self.add_segment(i)

    def add_segment(self, position):
        segment1 = Turtle("square")
        segment1.penup()
        segment1.color("white")
        segment1.goto(position)
        self.segments.append(segment1)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.fd(dis)

    def up(self):
        if self.head.heading()!= down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
