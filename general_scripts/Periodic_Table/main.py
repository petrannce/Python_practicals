import periodictable

element_name = input("Enter the name of the element: ").capitalize()
coding = getattr(periodictable, element_name, None)

if coding:
    print(f"Element: {coding.name}")
    print(f"Symbol: {coding.symbol}")
    print(f"Atomic Number: {coding.number}")
    print(f"Atomic Mass: {coding.mass}")
else:
    print(f"Element '{element_name}' not found in the periodic table.")
