import random
from turtle import Turtle, Screen, colormode
# import colorgram


# colors = colorgram.extract("spots.jpg", 30)
# rgb_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)

# list generated from spot.jpg picture by using colorgram package
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222),
              (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9),
              (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]


cookie = Turtle()

cookie.speed("fastest")
colormode(255)

# penup, so that the turtle doesn't draw black line while moving
cookie.penup()
# hiding the curser
cookie.hideturtle()
# changing the coordinates from (0,0) so that the pattern is easily shown
cookie.setheading(225)
cookie.forward(300)
cookie.setheading(0)
# used the below commented code to get the new coordinate value - (-212.13, -212.13)
# print(cookie.pos())
y_coordinate = -212.13


for rows in range(10):
    for column in range(10):
        # choosing random color from color_list
        cookie.dot(20, random.choice(color_list))
        cookie.forward(50)

    # adding 50 to the y coordinate so that the turtle moves 50 paces up
    y_coordinate += 50
    cookie.setpos(-212.13, y_coordinate)

screen = Screen()
screen.exitonclick()
