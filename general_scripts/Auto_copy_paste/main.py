import pyperclip as pc

text1 = input("Enter the first text: ")

pc.copy(text1)

text2 = pc.paste()

print("The copied text is: " + text2)