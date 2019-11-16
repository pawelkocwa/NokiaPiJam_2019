import math


def convertXY(x, y):
    L1 = 200  # mm
    L2 = 207  # mm
    p0 = x * x + y * y - L1 * L1 - L2 * L2
    # print("x: %f y: %f" % (x , y))
    # print("p0: %f" % p0)

    p1 = 2 * L1 * L2
    # print("p1: %f" % p1)

    beta = -math.acos(p0 / p1)
    # print("raw rad beta: %f" % beta)

    p2 = L2 * math.sin(beta)
    # print("p2: %f" % p2)

    p3 = L1 + L2 * math.cos(beta)
    # print("p3: %f" % p3)

    p4 = math.atan(y / x)
    # print("p4: %f" % p4)

    p5 = math.atan(p2 / p3)
    # print("p5: %f" % p5)

    alfa = (p4 - p5)
    # print("raw rad alfa: %f" % alfa)
    # print("raw rad beta: %f" % beta)

    alfa = alfa * (180 / math.pi)
    beta = beta * (180 / math.pi) * -1
    # print("raw deg alfa: %f" % alfa)
    # print("raw deg beta: %f" % beta)
    return (beta, alfa)  # x, y


def translate(angleXY):
    angle_x = angleXY[0]
    angle_y = angleXY[1]
    # print("raw alfa: %f beta: %f" % (angle_x, angle_y))

    y = 90 - angle_y
    x = angle_x - 180 + 45 + y
    # print("final x: %f y: %f" % (angle_x, angle_y))
    return (x, y)

# Example of use
# kat_xy = translate(convertXY(170, 0))
# kat_x = kat_xy[0]
# kat_y = kat_xy[1]
# print("x: %f y: %f" % (kat_x, kat_y))
