# import turtle

# turtle.speed(3)
# turtle.bgcolor('black')
# turtle.pensize(3)
# def func():
#     for i in range(200):
#         turtle.right(1)
#         turtle.forward(1)
# turtle.color ('purple' , 'pink')
# turtle.begin_fill()
# turtle.left(140)
# turtle.forward(111.65)
# func()
# turtle.left(120)
# func()
# turtle.forward(111.65)
# turtle.end_fill()
# turtle.hideturtle()
# turtle.done()

#----------------------------------->


# import turtle

# t = turtle.Turtle()

# for i in range(4):
#     t.forward(100)   # 100 pixels आगे बढ़ो
#     t.right(90)      # 90 degree दाईं तरफ घूमो

# turtle.done()

#------------------------------------------->

# import math
# from turtle import *
# def hearta(k):
#     return 15 * math.sin(k) ** 3
# def haertb(k):
#     return 12 * math.cos(k) - 5* \
#         math.cos(2 * k) - 2 * \
#         math.cos(3 * k) - \
#         math.cos(4 * k)
# speed(0)
# bgcolor("black")
# for i in range(6000):
#     goto(hearta(i) *20, haertb(i) * 20)
#     for j in range(1):
#         color("purple")
#     dot()
# goto(0,0)
# done()    

#------------------------------------------>

import time
import sys
def print_lyrics():
    lyrics = [
        "Oh, I used to say",
        "… I would never fall in love again until I found her",
        "I said, 'I would never fall unless it's you I fall into'",
        "I was lost within the darkness, but then I found her",
        "I found you"
        ]
    delays = [
        1.2,1.5, 1.5, 1.5, 2.0,
    ]
    print(" Untill I Found Her : \n")
    time.sleep(1.2)
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.9)
print_lyrics()