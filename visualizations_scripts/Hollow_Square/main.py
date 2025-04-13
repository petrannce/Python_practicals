import matplotlib.pyplot as plt

rows = 5
cols = 5
plt.figure(figsize=(6, 6))

for i in range(rows):
    for j in range(cols):
        # Create a hollow square using the rectangle function
        if (i == 0 or i == rows - 1) or (j == 0 or j == cols - 1):
            plt.scatter(j, -i, s=800, c='orange')

plt.xlim(-0.5, cols - 0.5)
plt.ylim(-rows + 0.5, 0.5)
plt.axis('off')
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title('Hollow Square Pattern Plot', fontsize=16, fontweight='bold')
plt.show()
# This code creates a hollow square pattern using matplotlib.