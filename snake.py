from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        for p in START:
            self.add_segment(p)
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        for seg in self.segments:
            if seg.heading() != DOWN:
                seg.setheading(UP)

    def down(self):
        for seg in self.segments:
            if seg.heading() != UP:
                seg.setheading(DOWN)

    def left(self):
        for seg in self.segments:
            if seg.heading() != RIGHT:
                seg.setheading(LEFT)

    def right(self):
        for seg in self.segments:
            if seg.heading() != LEFT:
                seg.setheading(RIGHT)

    def add_segment(self, pos):
        new = Turtle('square')
        new.color('white')
        new.up()
        new.teleport(pos[0], pos[1])
        self.segments.append(new)

    def extend(self):
        self.add_segment(self.segments[-1].position())