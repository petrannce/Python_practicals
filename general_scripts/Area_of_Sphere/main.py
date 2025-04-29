import math

def calculate_area_of_sphere(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

radius = float(input("Enter the radius of the sphere: "))

sphere_surface_area = calculate_area_of_sphere(radius)
print(f"The surface area of the sphere with radius {radius} is: {sphere_surface_area:.2f}")