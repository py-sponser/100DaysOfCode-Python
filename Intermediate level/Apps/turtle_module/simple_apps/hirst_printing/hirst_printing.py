import colorgram
from turtle import Screen, Turtle
import random
colors = colorgram.extract("spots.jpg",30)
final_colors = list()
for color in colors:
    final_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))


tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)
tim.penup()
def initiate():
    tim.hideturtle()
    tim.setheading((270 + 180) / 2)
    tim.forward(500)
    tim.setheading(0)


def dot():
    for i in range(15):
        tim.dot(20, random.choice(final_colors))
        tim.forward(50)

def draw_the_rest():
    tim.left(90)
    tim.forward(75)
    tim.left(90)
    tim.forward(750)
    tim.setheading(360)

initiate()
for i in range(10):
    dot()
    draw_the_rest()



screen.exitonclick()
