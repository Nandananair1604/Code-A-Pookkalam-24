from turtle import *

colours = ["cyan", "brown", "red", "blue", "brown", "yellow", "pink", "orange", "crimson", "tomato", "blue", "brown","darkmagenta","lawngreen","mediumpurple","deeppink","crimson","blue","cyan","pink"]
speed(0)
for j in range(20):
    k=10*j
    color(colours[j])
    for i in range(9):
        begin_fill()
        circle(200-k)
        end_fill()
        right(80)
exitonclick()
hideturtle()
