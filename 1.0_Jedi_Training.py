"""
1.0 Jedi Training (17pts)  Name: Logan Mills


1. Define Forking (1pt): 
Copying a repo to your local repos
2. Define Cloning (1pt): 
Cloning a repo to your local machine
3. Define Branching (1pt):
Creating separate copies of a repo on your local machine to test changes
4. Define Committing (1pt): 
Creating a save point that you can go back to
5. Define Merging (1pt): 
Combining the updated code in the original repository
6. Define Pushing (1pt):
Adding the changes to your local repository
7. Define Pull Request (1pt):
Requesting that the original owner merge your code with the original repository

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
"""
# Import needed modules

import turtle
import random

# Defining stuff

turtle.getscreen()
screen = turtle.Screen()
screen.screensize(400, 300)
screen.bgcolor("#1f1f1f")
turtle.pensize(1)
turtle.color("#000000")
turtle.speed(0)  # 0 is the fastest value, used to make it draw faster since it's a larger project
turtle.ht()

# The fun stuff

# Loop to add 250 stars, building the background

turtle.up()
turtle.color("white")
turtle.pensize(1)

stars = 0

while stars < 250:
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    size = random.randint(1, 5)
    turtle.goto(x, y)
    turtle.up()
    turtle.dot(size)
    stars += 1

# Setting location, prep in other words

turtle.up()
turtle.goto(-30, 0)
turtle.seth(210)
turtle.down()

# Outlining the body

turtle.color("black", "white")
turtle.begin_fill()
turtle.circle(50, 300)
turtle.end_fill()
turtle.up()
turtle.goto(-40, 1)
turtle.seth(-7)
turtle.down()
turtle.begin_fill()
turtle.circle(300, 13.5)
turtle.end_fill()

# Outlining the head

turtle.seth(80)
turtle.begin_fill()
turtle.circle(36, 200)
turtle.end_fill()
turtle.goto(-40, 4)
turtle.seth(-7)
turtle.begin_fill()
turtle.circle(300, 13.5)
turtle.end_fill()
turtle.up()

# Detail work

# Making the eyes or whatever they're supposed to be. Cameras maybe?

turtle.goto(-4, 12)
turtle.down()
turtle.color("black")
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

turtle.color("white")
turtle.up()
turtle.goto(-9, 18)
turtle.dot(4)
turtle.goto(-1, 24)
turtle.dot(2)
turtle.goto(-2, 24)
turtle.dot(2)
turtle.goto(-3, 25)
turtle.dot(2)
turtle.goto(-4, 25)
turtle.dot(2)
turtle.goto(-5, 25)
turtle.dot(2)
turtle.goto(-6, 25)
turtle.dot(2)
turtle.goto(1, 18)
turtle.dot(2)
turtle.goto(0, 17)
turtle.dot(2)
turtle.goto(0, 16)
turtle.dot(2)

turtle.color("red")

turtle.goto(-8, 22)
turtle.dot(1)
turtle.goto(-6, 22)
turtle.dot(1)

# Eye thing 2

turtle.color("black")

turtle.up()
turtle.goto(10, 7)
turtle.down()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.color("grey")

turtle.up()
turtle.goto(10, 8)
turtle.down()
turtle.begin_fill()
turtle.circle(4)
turtle.end_fill()

turtle.color("black")
turtle.up()
turtle.goto(10, 9)
turtle.down()
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()

turtle.color("white")
turtle.up()
turtle.goto(8, 10)
turtle.dot(1)
turtle.goto(12, 10)
turtle.dot(1)
turtle.goto(12, 13)
turtle.dot(1)

# The orange circles

# The easy one

turtle.up()
turtle.goto(-2, -93)
turtle.color("black", "orange")
turtle.down()
turtle.begin_fill()
turtle.circle(27)
turtle.end_fill()
turtle.color("black", "white")
turtle.goto(-2, -90)
turtle.begin_fill()
turtle.circle(21)
turtle.end_fill()

# The annoying ones that make me tear the hair out of my skull

turtle.up()
turtle.goto(-54, -40)
turtle.down()
turtle.seth(10)
turtle.color("black", "orange")
turtle.begin_fill()
turtle.circle(27, 100)
turtle.end_fill()
turtle.up()
turtle.goto(-53, -35)
turtle.down()
turtle.seth(10)
turtle.color("black", "white")
turtle.begin_fill()
turtle.circle(21, 100)
turtle.end_fill()

# An even MORE annoying orange circle (I didn't think it could get worse)

turtle.up()
turtle.goto(0, -2)
turtle.down()
turtle.seth(-90)
turtle.color("black", "orange")
turtle.begin_fill()
turtle.circle(27, 120)
turtle.end_fill()
turtle.up()
turtle.goto(6, -1)
turtle.down()
turtle.seth(-90)
turtle.color("black", "white")
turtle.begin_fill()
turtle.circle(23, 119)
turtle.end_fill()

# The antennas (Back to easy stuff)

turtle.up()
turtle.goto(0, 41)
turtle.down()
turtle.goto(0, 75)
turtle.up()
turtle.goto(-4, 43)
turtle.down()
turtle.goto(-4, 60)

# Detail lines and stuff

turtle.up()
turtle.goto(-28, 26)
turtle.down()
turtle.goto(-31, 23)
turtle.goto(-38, 24)

turtle.up()
turtle.goto(-34, 24)
turtle.down()
turtle.goto(-35, 20)

turtle.up()
turtle.goto(-39, 20)
turtle.down()
turtle.goto(-33, 19)
turtle.goto(-34, 15)
turtle.goto(-39, 15)

# Orange squares on head

turtle.color("black", "orange")

turtle.up()
turtle.goto(-39, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(-39, 11)
turtle.goto(-37, 11)
turtle.goto(-37, 4)
turtle.end_fill()

turtle.up()
turtle.goto(-35, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(-35, 11)
turtle.goto(-33, 10)
turtle.goto(-33, 4)
turtle.end_fill()

turtle.up()
turtle.goto(-31, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(-31, 10)
turtle.goto(-29, 10)
turtle.goto(-29, 4)
turtle.end_fill()

turtle.up()
turtle.goto(-26, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(-26, 10)
turtle.goto(-22, 9)
turtle.goto(-22, 4)
turtle.end_fill()

turtle.up()
turtle.goto(-20, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(-20, 9)
turtle.goto(-15, 9)
turtle.goto(-15, 4)
turtle.end_fill()

turtle.up()
turtle.goto(17, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(17, 9)
turtle.goto(25, 10)
turtle.goto(25, 4)
turtle.end_fill()

turtle.up()
turtle.goto(28, 4)
turtle.down()
turtle.begin_fill()
turtle.goto(28, 9)
turtle.goto(31, 10)
turtle.goto(25, 4)
turtle.end_fill()

# Line

turtle.up()
turtle.goto(-15, 4)
turtle.down()
turtle.goto(-15, 20)
turtle.seth(-90)
turtle.circle(10.2, -250)
turtle.goto(-1, 4)
turtle.up()
turtle.goto(5, 19)
turtle.down()
turtle.goto(10, 19)
turtle.seth(-180)
turtle.circle(7, -90)
turtle.goto(17, 4)

# Circle Connectors

turtle.up()
turtle.goto(-40, -32)
turtle.down()
turtle.goto(-24, -50)

turtle.up()
turtle.goto(20, -28)
turtle.down()
turtle.goto(10, -45)

turtle.up()
turtle.goto(-26, -83)
turtle.down()
turtle.goto(-29, -86)

turtle.up()
turtle.goto(17, -80)
turtle.down()
turtle.goto(23, -83)

# Grey head ring

turtle.color("black", "grey")

turtle.up()
turtle.goto(-30, 35)
turtle.begin_fill()
turtle.down()
turtle.seth(-15)
turtle.circle(100, 28)
turtle.goto(6, 41)
turtle.down()
turtle.seth(10)
turtle.circle(100, -15)
turtle.goto(-30, 35)
turtle.end_fill()

turtle.up()
turtle.goto(-5, 41)
turtle.down()
turtle.goto(-5, 32)

turtle.up()
turtle.goto(-15, 41)
turtle.down()
turtle.goto(-20, 33)

turtle.up()
turtle.goto(5, 41)
turtle.down()
turtle.goto(10, 33)

# Orange head ring

turtle.color("black", "orange")

turtle.up()
turtle.goto(-32, 30)
turtle.begin_fill()
turtle.seth(-15)
turtle.down()
turtle.circle(100, 10)
turtle.goto(-16, 24)
turtle.circle(100, -10)
turtle.end_fill()

turtle.up()
turtle.goto(22, 30)
turtle.begin_fill()
turtle.seth(10)
turtle.down()
turtle.circle(100, -10)
turtle.goto(6, 25)
turtle.circle(100, 10)
turtle.end_fill()

# The orange parts inside the circles

turtle.up()
turtle.goto(-10, -50)
turtle.down()
turtle.begin_fill()
turtle.goto(-7, -60)
turtle.goto(-5, -59)
turtle.goto(-5, -50)
turtle.end_fill()

turtle.up()
turtle.goto(-5, -90)
turtle.down()
turtle.begin_fill()
turtle.goto(-5, -80)
turtle.goto(-2, -79)
turtle.goto(0, -90)
turtle.end_fill()

turtle.up()
turtle.goto(15, -63)
turtle.down()
turtle.begin_fill()
turtle.goto(5, -66)
turtle.goto(5, -69)
turtle.goto(15, -68)
turtle.end_fill()

turtle.up()
turtle.goto(-25, -70)
turtle.down()
turtle.begin_fill()
turtle.goto(-15, -70)
turtle.goto(-15, -73)
turtle.goto(-24, -74)
turtle.end_fill()

turtle.up()
turtle.goto(28, -24)
turtle.down()
turtle.begin_fill()
turtle.goto(25, -15)
turtle.goto(28, -15)
turtle.goto(34, -23)
turtle.end_fill()

turtle.up()
turtle.goto(9, -7)
turtle.down()
turtle.begin_fill()
turtle.goto(17, -7)
turtle.goto(15, -3)
turtle.goto(7, -3)
turtle.end_fill()

turtle.up()
turtle.goto(-36, -12)
turtle.down()
turtle.begin_fill()
turtle.goto(-45, -15)
turtle.goto(-45, -18)
turtle.goto(-38, -18)
turtle.end_fill()

turtle.up()
turtle.goto(-50, -34)
turtle.down()
turtle.begin_fill()
turtle.goto(-50, -25)
turtle.goto(-49, -25)
turtle.goto(-47, -34)
turtle.end_fill()

# The grey inner circle details (I hate this part)

turtle.color("black", "grey")

turtle.up()
turtle.begin_fill()
turtle.goto(-20, -78)
turtle.seth(-60)
turtle.down()
turtle.circle(19, 45)
turtle.goto(-8, -80)
turtle.seth(-40)
turtle.circle(6, -180)
turtle.goto(0, -68)
turtle.seth(140)
turtle.circle(8, 140)
turtle.goto(-20, -78)
turtle.end_fill()

turtle.up()
turtle.begin_fill()
turtle.goto(5, -63)
turtle.down()
turtle.seth(130)
turtle.circle(13, 40)
turtle.goto(-3, -53)
turtle.seth(-180)
turtle.circle(13, -69)
turtle.goto(5, -63)
turtle.end_fill()

turtle.up()
turtle.goto(-50, -25)
turtle.begin_fill()
turtle.down()
turtle.seth(45)
turtle.circle(16, 45)
turtle.end_fill()

turtle.up()
turtle.goto(21, -1)
turtle.begin_fill()
turtle.down()
turtle.seth(-85)
turtle.circle(14, 90)
turtle.end_fill()

# Detail Circles

# Group 1

turtle.up()
turtle.goto(-22, -35)
turtle.down()
turtle.circle(2)

turtle.up()
turtle.goto(-14, -12)
turtle.down()
turtle.circle(2)

turtle.up()
turtle.goto(3, -33)
turtle.down()
turtle.circle(2)

# Group 2

turtle.up()
turtle.goto(27, -44)
turtle.down()
turtle.circle(2)

turtle.up()
turtle.goto(29, -70)
turtle.down()
turtle.circle(1)

# Group 3

turtle.up()
turtle.goto(-40, -49)
turtle.down()
turtle.circle(2)

turtle.up()
turtle.goto(-38, -74)
turtle.down()
turtle.circle(1)

# Signature

turtle.color("white")
turtle.up()
turtle.goto(-58, 120)
# turtle.write('Logan Mills',font=("Arial", 16, "normal"))

# Keep window open

turtle.mainloop()
