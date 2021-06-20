def draw_frame(t, frx):

    t.clear()
    t.penup()
    t.goto(-frx/2, -frx/2)
    t.pendown()
    t.clear()
    for i in range(4):
        t.forward(frx)
        t.left(90)


def calculate_angle_out(poly):
    inner_angle = 360 / poly
    run_angle = inner_angle

    while run_angle < 90:
        run_angle += inner_angle

    run_corner = poly

    while run_corner > 1:
        run_corner -= 4

    if run_corner == 1:
        return run_angle - inner_angle

    else:
        return run_angle
