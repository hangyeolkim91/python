# -*- coding: utf-8 -*-
class MyInt:


    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a +other

    def __mul__(self, other):
        return self.a*other

    def __sub__(self, other):
        return self.a - other

    def __truediv__(self, other):
        return self.a / other


a = MyInt(5)

print(a+5)
print(a*5)
print(a/5)
print(a-5)