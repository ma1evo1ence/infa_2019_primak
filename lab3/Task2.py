from graph import *
import math as m


def alien(x, y, size, mirror):
    body(x, y, size, mirror)
    apple(x + 3 * size * mirror, y - size * 3.2, size / 28, mirror)


def alien_noApple(x, y, size, mirror):
    body(x, y, size, mirror)


def apple(x, y, size, mirror):

    r = 25 * size
    penColor(245, 84, 84)
    penSize(0)
    brushColor(245, 84, 84)
    circle(x, y, r)

    penColor("black")
    penSize(2 * size)
    line(x, y - r * 0.8, x + r * 0.5 * mirror, y - r * 1.7)
    brushColor(100, 225, 100)
    penSize(size)
    polygon(curve(x + r * 0.1 * mirror, y - r * 1.1, size, not (mirror + 1)))


def ufo(x, y, size):
    penSize(0)
    brushColor(210, 250, 210)
    penColor(210, 250, 210)
    light = []
    light.append((x, y))
    light.append((x - 20 * size, y + 20 * size))
    light.append((x + 20 * size, y + 20 * size))
    polygon(light)
    brushColor(168, 168, 168)
    penColor(168, 168, 168)

    ellips(x, y, 20 * size, 5 * size, 0)

    brushColor(180, 220, 220)
    penColor(180, 220, 220)
    ellips(x, y - 3 * size, 12 * size, 4 * size, 0)
    brushColor('white')
    penColor('white')
    ellips(x, y + 3 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 8 * size, y + 2 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 8 * size, y + 2 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 14 * size, y + 0.05 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 14 * size, y + 0.05 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 5.5 * size, y + 2.5 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 3 * size, y + 3 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 5.5 * size, y + 2.5 * size, 1 * size, 0.33 * size, 0)    
    ellips(x + 3 * size, y + 3 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 10.5 * size, y + 1.6 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 10.5 * size, y + 1.6 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 12.3 * size, y + 1 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 12.3 * size, y + 1 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 15.7 * size, y - 0.7 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 15.7 * size, y - 0.7 * size, 1 * size, 0.33 * size, 0)
    ellips(x - 15.2 * size, y - 1.9 * size, 1 * size, 0.33 * size, 0)
    ellips(x + 15.2 * size, y - 1.9 * size, 1 * size, 0.33 * size, 0)


def curve(x, y, size, mirror):
    if mirror:
        m = 1
    else:
        m = -1

    res = []
    for i in range(int(40 * size)):
        res.append((x + m * i * 0.6 * size, y + (-5 * size) * (i**0.3)))
    return res


def ellips(x, y, a, b, f):
    f = f * m.pi / 180
    x_e = [i for i in range(-a, a)]
    y1, y2 = [], []
    for i in range(len(x_e)):
        xy1 = [x_e[i], b * (1 - (x_e[i] / a)**2)**0.5]
        xy2 = [x_e[i], -b * (1 - (x_e[i] / a)**2)**0.5]
        xy1 = [xy1[0] * m.cos(f) - xy1[1] * m.sin(f), xy1[0]
               * m.sin(f) + xy1[1] * m.cos(f)]
        xy2 = [xy2[0] * m.cos(f) - xy2[1] * m.sin(f), xy2[0]
               * m.sin(f) + xy2[1] * m.cos(f)]
        y1.append((xy1[0] + x, xy1[1] + y))
        y2.append((xy2[0] + x, xy2[1] + y))
    y2 = y2[::-1]
    polygon(y1 + y2)


def body(x_b, y_b, S, mirror):
    color = '#C7F971'
    penColor(color)
    brushColor(color)
    ellips(x_b, y_b, S, 1.5 * S // 1, 0)  # main body

    ellips(x_b + 1.1 * S * mirror, y_b - 1.2 * S, S // 2, S // 3, 0)
    ellips(x_b - 1.1 * S * mirror, y_b - 0.7 * S, S // 2, S // 3, 0)
    ellips(x_b - 1.5 * S * mirror, y_b - 0.2 *
           S, S // 2, S * 1.2 // 2, 30 * mirror)
    ellips(x_b - 2.5 * S * mirror, y_b + 0.5 * S,
           S // 2, S * 0.8 // 1, -100 * mirror)

    ellips(x_b + 2.1 * S * mirror, y_b - 1.4 *
           S, int(S / 1.1), int(S // 2.5), -20 * mirror)
    ellips(x_b + 2.5 * S * mirror, y_b - 2.1 * S,
           int(S / 1.6), int(S / 2.4), 10 * mirror)
    ellips(x_b, y_b + S * 1.5, S, S, 0)

    ellips(x_b + S * mirror, y_b + S * 2.7, S //
           2, S // 1, -10 * mirror)  # left_leg
    ellips(x_b + S * mirror, y_b + S * 4, S // 2, S // 1, -10 * mirror)
    ellips(x_b + 1.6 * S * mirror, y_b + S * 5,
           S // 2, S * 0.9 // 1, -90 * mirror)

    ellips(x_b - S * mirror, y_b + S * 2.7, S //
           2, S // 1, 10 * mirror)  # right_leg
    ellips(x_b - 1.3 * S * mirror, y_b + S * 4, S // 2, S // 1, 10 * mirror)
    ellips(x_b - 1.8 * S * mirror, y_b + S * 5,
           S // 2, S * 0.9 // 1, 70 * mirror)

    penSize(S // 2)  # head
    polygon([(x_b + 1.6 * S, y_b - 3 * S),
             (x_b, y_b + 1 * S - 3 * S), (x_b - 1.6 * S, y_b - 3 * S)])
    rectangle(x_b - 0.15 * S, y_b + 1 * S - 3 * S,
              x_b + 0.15 * S, y_b + 3 * S - 3 * S)
    penSize(0.5 * S)
    line(x_b + 1.6 * S, y_b - 3 * S, x_b + 3.1 * S, y_b - 3.5 * S)
    line(x_b - 1.6 * S, y_b - 3 * S, x_b - 2.2 * S, y_b - 4.2 * S)

    brushColor('red')
    penSize(0.15 * S)
    circle(x_b + 2.6 * S, y_b - 3.5 * S, 0.3 * S)
    circle(x_b - 2.3 * S, y_b - 4.2 * S, 0.3 * S)

    penSize(1)
    brushColor('black')
    circle(x_b + 1 * S, y_b - 2.8 * S, S // 2)
    circle(x_b - 1 * S, y_b - 2.8 * S, S // 2)
    brushColor('white')
    ellips(x_b + 1.2 * S * mirror, y_b - 2.9 * S, S // 6, S // 4, 0)
    ellips(x_b - 0.8 * S * mirror, y_b - 2.9 * S, S // 6, S // 4, 0)


def cloud(x, y, S, color):
    colinc = 10
    brushColor(color + colinc, color + colinc, color + colinc)
    penColor(color + colinc, color + colinc, color + colinc)
    ellips(x - 1.2 * S, y, S, S, 0)
    ellips(x, y, S, S, 0)
    ellips(x + 1.2 * S, y, S, S, 0)


brushColor(70, 50, 90)
rectangle(0, 0, 500, 400)

brushColor(59, 135, 59)
rectangle(0, 400, 500, 800)


brushColor(255, 244, 164)
circle(350, 120, 100)

for i in range(200):
    x_star = randint(0, 500)
    y_star = randint(0, 400)
    penColor(255, 244, 164)
    point(x_star, y_star)
    point(x_star + 1, y_star)
    point(x_star - 1, y_star)
    point(x_star, y_star + 1)
    point(x_star, y_star - 1)

for i in range(100):
    cloud(350, 180, 70 - i // 2, i)
for i in range(100):
    cloud(400, 40, 50 - i // 2, i)
for i in range(70):
    cloud(180, 30, 60 - i // 2, i)


ufo(440, 100, 3)
ufo(50, 300, 5)
ufo(280, 280, 7)


alien(60, 360, 15, -1)
alien(330, 420, 20, 1)
alien(460, 370, 14, -1)
alien_noApple(240, 470, 13, 1)


run()
