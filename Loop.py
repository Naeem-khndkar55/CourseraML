import turtle

for _ in range(3): #for loop
    print("hi")


wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess=turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
elan=turtle.Turtle()
distance =50
dist=5
tess.up()
for _ in range(30):
    tess.stamp()
    tess.forward(dist)
    tess.right(24)
    dist+=2


angle=90
for _ in range(10):
    elan.forward(distance)
    elan.right(angle)
    distance+=10
    angle =angle-3

wn.exitonclick()