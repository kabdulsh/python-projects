import CustomExceptions
import math

class RightAngleTriangle:
    def __init__(self):
        self._length_a = 0
        self._length_b = 0
        self._length_c = 0

    def set_lengths(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if (a**2) + (b**2) != (c**2):
            raise CustomExceptions.InvalidHypotenuse("")

    def get_area(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

        if self.a == 0 or self.b == 0 or self.c == 0:
            raise CustomExceptions.LengthNotDefined("")

        area = (self.a * self.b) / 2

        return "Area: %.2f" % area

class Rectangle:
    def __init__(self):
        self._length = 0
        self._width = 0

    def set_length(self, length):
        self._length = length

    def set_width(self, width):

        self._width = width

    def get_area(self, length, width):

        if self._length == 0 or self._width == 0:
            raise CustomExceptions.LengthNotDefined("")

        area = self._length * self._width

        return "Area: %.2f" % area

class Circle:

    def __init__(self):
        self._radius = 0

    def set_radius(self, radius):

        self.radius = radius
        return radius

    def get_area(self):

        if self.radius == 0:
            raise CustomExceptions.LengthNotDefined("")

        area = math.pi * (self.radius ** 2)

        return "Area: %.2f\n" % area