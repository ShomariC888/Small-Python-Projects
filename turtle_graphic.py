from turtle import*
import colorsys
bgcolor('black')
tracer(50)
def draw():
    h = 0.4
    n = 200
    for i in range(280):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 1/n
        up()
        goto(0,0)
        down()
        color(c)
        pensize(3)
        fd(i)
        circle(i/1.5, 100)
        circle(i/3, 100)
draw()
done()