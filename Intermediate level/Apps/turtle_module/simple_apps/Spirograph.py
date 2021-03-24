from turtle import Turtle, Screen
import random
def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

screen = Screen()
tim = Turtle()
screen.colormode(255)

tim.speed(0)
def draw_spirograph(gap):
    for i in range(int(360/gap)):
        tim.pencolor(get_random_color())
        tim.circle(100)
        tim.left(gap)

draw_spirograph(5)

screen.exitonclick()
