import math as m

'''
def f1(a=0, b=0, c=0):
    return (a**b, b**c, a-c)
a1, b1, c1 = f1(3,2,6)
#print (a1, b1 ,c1)
'''


def line(a=0, b=0):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        if not (a == 0):
            return [-b / a]
    return []


def square(a=0, b=0, c=0):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (float, int)):
        if not (a == 0):
            D = b ** 2 - 4 * a * c
            if D > 0:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                return [x1, x2]
            elif D == 0:
                x1 = -b / (2 * a)
                return [x1]
        # если уравнение оказалось линейным
        elif a == 0:
            return line(b, c)
    return []


def cube(a=0, b=0, c=0, d=0):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(c, (float, int)) and isinstance(d, (float, int)):
        if a == 0:
            return square(b, c, d)
        if not (a == 0) and (d == 0):
            dis = -4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 + 18 * a * b * c * d - 27 * a ** 2 * d ** 2
            if dis > 0:
                x1 = 0
                x2 = (-b + d ** 0.5) / (2 * a)
                x3 = (-b - d ** 0.5) / (2 * a)
                return [x1, x2, x3]
            if dis == 0:
                x2 = -b / (2 * a)
                return [x2]
        p = (3 * a * c - b ** 2) / (3 * a ** 2)
        q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
        S = (4 * (3 * a * c - b ** 2) ** 3 + (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) * (
                2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d)) / (2916 * a ** 6)
        y1 = 0
        y2 = 0
        if S < 0:
            if q < 0:
                t = m.atan(-2 * (-S ** 0.5) / q)
                if q > 0:
                    t = m.atan(-2 * (-S ** 0.5) / q) + m.pi
                if q == 0:
                    t = m.pi / 2
                x1 = 2 * (-p / 3) ** 0.5 * m.cos(t / 3) - b / (3 * a)
                x2 = 2 * (-p / 3) ** 0.5 * m.cos((t + 2 * m.pi) / 3) - b / (3 * a)
                x3 = 2 * (-p / 3) ** 0.5 * m.cos((t + 4 * m.pi) / 3) - b / (3 * a)
                if q == 0:
                    x3 = -b / (3 * a)
                return [x1, x2, x3]
        elif S > 0:
            if (-q / 2 + S ** 0.5) > 0:
                y1 = m.exp(m.log(m.fabs(-q / 2 + S ** 0.5)) / 3)
            if (-q / 2 + S ** 0.5) < 0:
                y1 = -m.exp(m.log(m.fabs(-q / 2 + S ** 0.5)) / 3)
            if (-q / 2 + S ** 0.5) == 0:
                y1 = 0
            if (-q / 2 - S ** 0.5) > 0:
                y2 = m.exp(m.log(m.fabs(-q / 2 - S ** 0.5)) / 3)
            if (-q / 2 - S ** 0.5) < 0:
                y2 = -m.exp(m.log(m.fabs(-q / 2 - S ** 0.5)) / 3)
            if (-q / 2 - S ** 0.5) == 0:
                y2 = 0
            Re = -(y1 + y2) / 2 - b / a / 3
            Im = (y1 - y2) * 3 ** 0.5 / 2
            x1 = y1 + y2 - b / a / 3
            x2 = complex(Re, Im)
            x3 = complex(Re, -Im)
            return [x1, x2, x3]
        elif S == 0:
            if q < 0:
                y1 = m.exp(m.log(m.fabs(-q / 2)) / 3)
            if q > 0:
                y1 = -m.exp(m.log(m.fabs(-q / 2)) / 3)
            if q == 0:
                y1 = 0
            x1 = 2 * y1 - b / a / 3
            x2 = -y1 - b / a / 3
            x3 = -y1 - b / a / 3
            return [x1, x2, x3]
    return []


'''
print(line(45, 9))
print(square(2, 45, 9))
print(cube(0, 2, 45, 9))
print(cube(1, 6, -15, 22))  # С комплексными корнями
'''