# Exercise 1 & 2
class Bus(object):
    counter = 0

    def __init__(self, num_of_seats, color, driver_name):
        self.num_of_seats = num_of_seats
        self.color = color
        self.driver_name = driver_name
        Bus.counter += 1

    def change_color(self, recolor):
        self.color = recolor


from math import pi


class Shapes(object):

    def __init__(self, shape_type, name, sides):
        self.type = shape_type
        self.name = name
        self.sides = sides

#
# class Circle(Shapes):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         circle_area = pi*(self.radius**2)
#         return circle_area
#
#
# class Triangle(Shapes):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         triangle_area = 0.5*self.base*self.height
#         return triangle_area
#
#
# class Rectangle(Shapes):
#     def __init__(self, length, width):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         rectangle_area = self.width*self.length
#         return rectangle_area
#
#
# class Square(Shapes):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         square_area = self.side**2
#         return square_area
