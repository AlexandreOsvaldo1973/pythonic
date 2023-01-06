from math import sqrt

def f(t):
    return sqrt(abs(t)) + 5 * t ** 3

a = [float(input()) for _ in range(11)]
for i, t in reversed(list(enumerate(a))):
    y = f(t)
    print(i, 'TOO LARGE' if y > 400 else y)