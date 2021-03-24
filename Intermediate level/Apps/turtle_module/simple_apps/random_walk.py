from turtle import Screen, Turtle
import random

angels = [0,90,180,270]
tim = Turtle()
screen = Screen()

def get_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(200):
    movements = [tim.right,tim.left]
    a_move = random.choice(movements)(random.choice(angels))
    # or > a_move = tim.setheading(random.choice(angels))
    distance = random.randint(40,100)
    screen.colormode(255)
    color = get_random_color()
    tim.pencolor(color)
    tim.speed(0)
    tim.width(10)
    tim.forward(distance)
