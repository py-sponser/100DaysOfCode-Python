from turtle import Screen, Turtle
import random


class DrawShapes:
    """Draw shapes (same distance of sides: square, hexagon ..), numbers of sides need to be given, each vector distance, reverse boolean variable to draw the same shape in negative direction with original positive direction"""

    def __init__(self, sides=None, degree=360, distance=100, reverse=False, dash=False):
        self.tim = Turtle()

        self.tim.shape("turtle")
        self.colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
                       "SlateGray",
                       "SeaGreen"]
        self.sides = sides
        self.degree = degree
        self.distance = distance
        self.reverse_shapes = reverse
        self.dash = dash
        self.dash_distance = None

    def dashed_line(self, distance):
        """Draws a dash line, distance of a side need to be given"""
        for count in range(distance):
            self.tim.pendown()  # draw the following forward distance
            self.tim.forward(distance)
            self.tim.penup()  # skip drawing the following distance
            self.tim.forward(distance)

    def dashed_shapes(self, distance, dash_distance):
        """Draw a dashed shape, distance of each side need to be given, also distance between each dash"""
        self.distance = distance
        self.dash = True
        self.dash_distance = dash_distance
        for i in range(3, 11):
            self.sides = i
            self.tim.color(random.choice(self.colors))
            self.draw_shape(self.degree)
            self.draw_shape(self.degree * -1)

        super().__init__()  # resetting values

    def draw_shape(self, degree=360, reverse=False,dash_distance=8):
        """"Draw shapes, depends on given number of sides, distance, degree of angels"""
        self.dash_distance = dash_distance
        for i in range(self.sides):
            if self.dash:
                self.dashed_line(self.dash_distance)
            elif not self.dash:
                self.tim.forward(self.distance)

            if self.reverse_shapes:  # reverse parameter of  single shape
                self.tim.right((degree * -1) / self.sides)
                continue

            elif not self.reverse_shapes:
                self.tim.right(degree / self.sides)
                continue

            if reverse: # reverse parameter of multiple shapes
                self.tim.right(degree / self.sides)

            elif not reverse:
                self.tim.right(degree / self.sides)





        super().__init__()

    def shapes_with_OptionalReverse(self):
        """Draw shapes with optional reverse, depends on given value of angel"""
        for i in range(3, 11):
            self.sides = i
            self.tim.color(random.choice(self.colors))
            if self.reverse_shapes:
                self.draw_shape(self.degree, reverse=True) # reverse True, start drawing from top first
                self.draw_shape(self.degree * -1,reverse=True) # draw the shape in the opposite direction
            else:
                self.draw_shape(self.degree) # reverse is False as default, start drawing from bottom first
                self.draw_shape(self.degree*-1) # draw the shape in the opposite direction
        super().__init__()  # resetting values

    def set_turtle_center(self):
        self.tim.forward(self.distance / 2)

    def __del__(self):
        self.screen = Screen()
        self.screen.exitonclick()


draw = DrawShapes(sides=4, distance=100, reverse=False, dash=True)
draw.shapes_with_OptionalReverse()
