import random
from turtle import Turtle, Screen


colors = [['Green', 'Wahaj'], ['Red','Daria'], ['Black', 'Zohan'], ['Blue', 'Romaisa'], ['Pink','Wajeeh']]
names = ['Wahaj', 'Daria', 'Zohan', 'Romaisa', 'Wajeeh']

screen = Screen()
user_choice = screen.textinput("Babies Race", "Write 'play' to Start! ")

screen.setup(500, 400)
height = 120
racers = []
is_race_on = False

for turtle_index in range(0, 5):
    t = Turtle(shape='turtle')
    t.color(colors[turtle_index][0])
    t.penup()
    t.goto(-240, height)
    t.write(colors[turtle_index][1], font=("Verdana", 15, "normal"))
    height -= 60
    racers.append(t)

if user_choice:
    is_race_on = True

while is_race_on:
    for ind in range(0, len(racers)):
        racer = racers[ind]
        if racer.xcor() > 230:
            is_race_on = False
            new_turtle = Turtle(shape="blank")
            new_turtle.penup()
            new_turtle.goto(-240, 170)
            name = colors[ind][1]
            new_turtle.write(f"{name} is the winner of the race.", font=("Verdana", 15, "normal"))

        random_number = random.randint(0, 10)
        racer.forward(random_number)

screen.exitonclick()