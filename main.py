import turtle
import functions
import math

s = turtle.getscreen()
t = turtle.Turtle()
s.bgcolor('lightblue')
outer_corner = 0


def goto_routine(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


frame_size = int(input("Frame Size? "))
t.speed(200)
functions.draw_frame(t, frame_size)

goto_routine(0, frame_size / 2)

poly = int(input("How many corners? "))
is_odd = poly % 2
turn_angle = 360 / poly
inner_angle = (poly - 2) / poly * 180

t.right((180 - inner_angle) / 2)

if is_odd:
    widest = functions.calculate_angle_out(poly) - 90
    math.radians(widest)
    r_u = (frame_size / 2) / math.cos(math.radians(widest))
    outer_corner = widest
    move_len = 2 * r_u * math.sin(math.pi / poly)

else:
    move_len = frame_size * math.sin(math.pi / poly)

for i in range(poly):
    t.forward(move_len)
    t.right(turn_angle)

goto_routine(0, 0)
t.setheading(-outer_corner)
t.forward(frame_size / 2 - 10)

turtle.Screen().exitonclick()
