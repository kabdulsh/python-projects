import Shapes
import CustomExceptions


def menu():

    choice = ""
    choices = ["a", "b", "c", "d"]

    while choice not in choices:

        print("a) create a right angle triangle")
        print("b) create a rectangle")
        print("c) create a circle")
        print("d) QUIT")

        choice = input()

    return choice


choice = ""

while choice != "d":

    try:
        choice = menu()

        if choice == "a":
            example_right_angle = Shapes.RightAngleTriangle()
            a = int(input("length of a\n"))
            b = int(input("length of b\n"))
            c = int(input("length of c\n"))
            example_right_angle.set_lengths(a, b, c)
            print(example_right_angle.get_area(a, b, c))
        if choice == "b":
            example_rectangle = Shapes.Rectangle()
            length = int(input("length\n"))
            width = int(input("width\n"))
            example_rectangle.set_length(length)
            example_rectangle.set_width(width)
            print(example_rectangle.get_area(length, width))
        if choice == "c":
            example_circle = Shapes.Circle()
            radius = int(input("radius\n"))
            example_circle.set_radius(radius)
            print(example_circle.get_area())
        if choice == "d":
            break
    except CustomExceptions.InvalidHypotenuse:
        print("please enter valid length for hypotenuse")
    except CustomExceptions.LengthNotDefined:
        print("please enter non-zero value")
