import turtle
import os
import random
import time

cases=0
casualties=10

win=turtle.Screen()
win.title("PANACEA")
win.setup(width=800,height=600)
win.bgpic("background.gif")
win.tracer(0)


win.register_shape("earth.gif")
win.register_shape("earth.gif")
win.register_shape("frontliners.gif")
win.register_shape("coronavirus.gif")




victim=turtle.Turtle()
victim.speed(0)
victim.shape("earth.gif")
victim.penup()
victim.goto(0,-250)
victim.direction="stop"


heroes = []

for i in range(3):
    hero=turtle.Turtle()
    hero.speed(0)
    hero.shape("frontliners.gif")
    hero.penup()
    hero.goto(-100,250)
    hero.speed = (random.randint(1,2))
    heroes.append(hero)


villans = []

for i in range(3):
    villan=turtle.Turtle()
    villan.speed(0)
    villan.shape("coronavirus.gif")
    villan.penup()
    villan.goto(100,250)
    villan.speed = (random.randint(1,2))
    villans.append(villan)




pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.goto(0,260)
font = ("courier",24,"normal")
pen.write("cases: {} casualties: {}".format(cases,casualties),align="center",font=font)


def go_left():
    victim.direction="left"

def go_right():
    victim.direction="right"


win.listen()
win.onkeypress(go_left,"Left")
win.onkeypress(go_right,"Right")


while True:
    win.update()

    if victim.direction == "left":
        x = victim.xcor()
        x -= 1
        victim.setx(x)

    if victim.direction == "right":
        x = victim.xcor()
        x += 1
        victim.setx(x)

    for hero in heroes:
        y = hero.ycor()
        y -= hero.speed
        hero.sety(y)

        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            hero.goto(x,y)

        if hero.distance(victim)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            hero.goto(x,y)
            cases +=10
            pen.clear()
            pen.write("cases: {} casualties: {}".format(cases,casualties),align="center",font=font)


    for villan in villans:
        y = villan.ycor()
        y -= villan.speed
        villan.sety(y)

        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            villan.goto(x,y)

        if villan.distance(victim)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            villan.goto(x,y)
            cases -=10
            casualties -=1
            pen.clear()
            pen.write("cases: {} casualties: {}".format(cases,casualties),align="center",font=font)



win.mainloop()