import random


class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __add__(self, other):
        return A(self.field1 ** other.field1, self.field2 ** other.field2)

    def __str__(self):
        return str(self.field1) + ' ' + str(self.field2)


class B:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2

    def __add__(self, other):
        if random.randint(1, 2) == 1:
            return B(self.field1, other.field2)
        return B(other.field1, self.field2)

    def __str__(self):
        return self.field1 + ' ' + self.field2


class Rectangle:
    def __init__(self, width, height, sign):
        self.w = int(width)
        self.h = int(height)
        self.s = str(sign)

    def __str__(self):
        rect = []
        for i in range(self.h):
            rect.append(self.s * self.w)
        rect = '\n'.join(rect)
        return rect

    # method __add__() is called automatically when program see '+'
    # if it is defined in class, of course
    # and then method execute operation which was defined
    def __add__(self, other):
        return Rectangle(self.w + other.w, self.h + other.h, self.s)
