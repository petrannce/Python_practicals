import getpass

# This code is a simple password authentication script that checks the entered username and password against a predefined dictionary of usernames and passwords.
database = {'Pythonpracticals': 'Pythonpracticals123', 'Python': 'Python123'}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# The script uses the getpass module to securely prompt for a password without echoing it to the console.
for i in database:
    if username == i:
        password_1 = database.get(i)
        password_2 = getpass.getpass("Enter your password: ")
        if password_1 == password_2:
            print("Login successful!")
            break
        else:
            print("Incorrect password!")
            break
else:
    print("Login failed!")
# This script uses the getpass module to securely prompt for a password without echoing it to the console.