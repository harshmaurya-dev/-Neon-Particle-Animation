import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Particle Animation")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

particles = []

for i in range(80):
    p = turtle.Turtle()
    p.shape("circle")
    p.color(random.choice(["cyan", "magenta", "yellow", "lime"]))
    p.penup()
    p.goto(random.randint(-300,300), random.randint(-250,250))
    p.speed(0)
    particles.append(p)

angle = 0

while True:
    for i, p in enumerate(particles):
        x, y = p.position()

        new_x = x + math.sin(angle + i) * 2
        new_y = y + math.cos(angle + i) * 2

        if abs(new_x) > 350 or abs(new_y) > 300:
            p.goto(random.randint(-300,300), random.randint(-250,250))
        else:
            p.goto(new_x, new_y)

    angle += 0.05