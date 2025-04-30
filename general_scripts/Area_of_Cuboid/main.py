import math

def calculate_cuboid_surface_area(length, width, height):
   
   surface_area = 2 * (length * width + length * height + width * height)
   return surface_area

length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

surface_area = calculate_cuboid_surface_area(length, width, height)
print(f"The surface area of the cuboid is: {surface_area} square units")