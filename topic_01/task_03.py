import math


def discr(a, b, c):
    d = b*b - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        return "Немає коренів"


a = int(input("What's a: "))
b = int(input("What's b: "))
c = int(input("What's c: "))

D = discr(a, b, c)

print(D)