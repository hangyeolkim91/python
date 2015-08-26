__author__ = 'user'
import math

def get_star(x):
    s = []
    n= math.ceil(x/2)

    for i in range(n):
        s.append(('*'*(2*i+1)).center(x))

    s += s[-2::-1]
    s = '\n'.join(s)
    return s


print(get_star(9))
