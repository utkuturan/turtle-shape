import turtle as t
import random


tim = t.Turtle()

colours = ["aquamarine", "crimson","medium blue","chartreuse","purple","deep pink","light coral","yellow","light sky blue","dark green","dark slate blue"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))