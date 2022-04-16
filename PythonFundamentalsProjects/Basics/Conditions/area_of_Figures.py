from math import pi
figure = input("enter figure: ")
if figure == "square":
    square_side = float(input("enter square side: "))
    square_area = square_side * square_side
    print(f"the square area is: {square_area:.3f}")
elif figure == "rectangle":
    rectangle_side = float(input())
    rectangle_Side = float(input())
    rectangle_area = rectangle_side * rectangle_Side
    print(f"{rectangle_area: .3f}")
elif figure == "circle":
    radius = float(input())
    A = pi * radius * radius
    print(f"{A: .3f}")
elif figure == "triangle":
    triangle_side = float(input())
    length_towards_side = float(input())
    triangle_area = (triangle_side * length_towards_side) / 2
    print(f"{triangle_area: .3f}")

