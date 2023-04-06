import turtle
from turtle import *
import random
import time

while True:
    screen = turtle.Screen()
    sharkspd = 5


    def red_up():
        global sharkspd
        if shark.ycor() < 175:
            shark.setheading(90)
            shark.fd(sharkspd)


    def red_down():
        global sharkspd
        if shark.ycor() > -195:
            shark.setheading(270)
            shark.fd(sharkspd)


    def red_left():
        global sharkspd
        if shark.ycor() > -195:
            shark.setheading(270)
            shark.fd(sharkspd)


    def red_right():
        global sharkspd
        if shark.ycor() < 175:
            shark.setheading(90)
            shark.fd(sharkspd)


    screen.bgcolor("cyan")

    shark = turtle.Turtle()
    shark.up()
    shark.speed("fastest")
    shark.shape("circle")
    shark.goto(-270, 0)
    shark.speed(0)
    shark.color('green')
    shark.penup();

    screen.onkey(red_up, 'Up')
    screen.onkey(red_down, 'Down')
    screen.onkey(red_left, 'Right')
    screen.onkey(red_right, 'Left')

    fish = turtle.Turtle()
    fish.up()
    fish.color("dark orange")
    fish.speed("fastest")
    fish.shape('square')

    x = random.randint(270, 300)
    y = random.randint(-200, 190)
    fishX = int(fish.xcor())
    sharkX = int(shark.xcor())
    fishY = int(fish.ycor())
    sharkY = int(shark.ycor())

    scoreboard = turtle.Turtle()
    scoreboard.hideturtle()

    score = 0

    gameoverturt = turtle.Turtle()
    gameoverturt.hideturtle()
    gameoverturt.up()
    intspd = 5

    status = False
    game_over = False


    def gameover():
        global game_over
        if game_over == True:
            gamebox.clear()
            shark.hideturtle()
            fish.hideturtle()
            scoreboard.clear()
            screen.bgcolor("red")
            gameoverturt.goto(-230, 0)
            gameoverturt.write("GAME OVER!", font=("Verdana", 50, "Bold"))
            gameoverturt.goto(-170, -100)
            gameoverturt.write("Your final score was: " + str(score), font=("Verdana", 20, "Bold"))


    incrange = 30


    def fish_spawn():
        global status
        global fish
        fishX = int(fish.xcor())
        sharkX = int(shark.xcor())
        fishY = int(fish.ycor())
        sharkY = int(shark.ycor())
        global incrange
        global game_over
        global sharkspd
        if fish.xcor() > -300:
            global intspd
            fish.setheading(180)
            fish.fd(intspd)
        if fish.xcor() in range((sharkX - incrange), (sharkX + 30)) and fish.ycor() in range((sharkY - 15),
                                                                                             (sharkY + 15)):

            global score
            score += 1
            scoreboard.reset()
            scoreboard.hideturtle()
            x = random.randint(270, 300)
            y = random.randint(-200, 180)
            while 20 >= y >= -20:
                y = random.randint(-200, 180)
            fish.goto(x, y)
            scoreboard.speed("fastest")
            scoreboard.up()
            scoreboard.goto(190, 190)
            scoreboard.write(("Score: " + str(score)), font=("Arial", 18, "Normal"))
            scoreboard.up()
            intspd += 1
            sharkspd += 1
            incrange += 1
            status = False
        if fish.xcor() <= -295:
            game_over = True
            status = True


    gamebox = turtle.Turtle()
    gamebox.hideturtle()
    gamebox.speed(100)
    gamebox.up()
    gamebox.goto(-310, 185)
    gamebox.setheading(0)
    gamebox.down()
    gamebox.fd(620)
    gamebox.setheading(270)
    gamebox.fd(390)
    gamebox.setheading(180)
    gamebox.fd(620)
    gamebox.setheading(90)
    gamebox.fd(390)

    deadline = turtle.Turtle()
    deadline.color("red")
    deadline.speed(100)
    deadline.width(3)
    deadline.hideturtle()
    deadline.up()
    deadline.goto(-309, 185)
    deadline.setheading(270)
    deadline.down()
    deadline.fd(388)

    Screen().listen()
    Screen().mainloop()

    while status == False:
        fish_spawn()
        gameover()
    while True:
        answer = str(input('\n Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        screen.clear()
        continue
    else:
        print("Goodbye")
        break
