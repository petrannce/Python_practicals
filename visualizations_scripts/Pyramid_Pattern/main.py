import matplotlib.pyplot as plt

rows = 10
plt.figure(figsize=(8, 8))

for i in range(rows):
    for j in range(2*i + 1):
        x = j - i
        y = -i
        plt.scatter(x, y, color='blue', s=100, edgecolor='black')

plt.xlim(-rows, rows)
plt.ylim(-rows, 1)

plt.axis('off')
plt.title('Pyramid Pattern', fontsize=16, color='navy', fontweight='bold', pad=20)
plt.show()