import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
  """
  Calculates the sigmoid value for a given input x.
  """
  return 1 / (1 + np.exp(-x))

# Generate x values from -10 to 10 with 100 points
x = np.linspace(-10, 10, 100)
# Calculate corresponding sigmoid values
y = sigmoid(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sigmoid Function', color='blue')
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.title('Sigmoid Activation Function')
plt.grid(True)
plt.legend()
plt.show()