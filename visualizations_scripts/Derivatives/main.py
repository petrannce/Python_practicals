import numpy as np
import matplotlib.pyplot as plt

# Define a function
def f(x):
    return x**3 - 3*x + 1

# Calculate the derivative numerically
def derivative(func, x, h=0.001):
    return (func(x + h) - func(x)) / h

# Generate x values
x = np.linspace(-3, 3, 400)

# Calculate y values and derivative values
y = f(x)
y_prime = derivative(f, x)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the function
plt.plot(x, y, label='f(x) = x^3 - 3x + 1')

# Plot the derivative
plt.plot(x, y_prime, label="f'(x) ≈ 3x^2 - 3", linestyle='--')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and its Derivative')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()