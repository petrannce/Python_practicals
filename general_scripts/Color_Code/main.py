import webcolors

color_name = input("Enter a color name: ")

try:
    hex_code = webcolors.name_to_hex(color_name.lower())
    print(f"The hex code for '{color_name}' is: {hex_code}")
except ValueError:
    print("Invalid color name. Please try again.")
    