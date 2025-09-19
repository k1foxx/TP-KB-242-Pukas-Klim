def discr(a, b, c):
    return b*b - 4*a*c

a = int(input("What's a: "))
b = int(input("What's b: "))
c = int(input("What's c: "))

D = discr(a, b, c)

print(D)