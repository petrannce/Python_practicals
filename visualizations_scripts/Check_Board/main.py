import numpy as np
import matplotlib.pyplot as plt

def plot_checkerboard(size=8):
    board = np.indices((size, size)).sum(axis=0) % 2

    plt.figure(figsize=(6, 6))
    plt.imshow(board, cmap='gray', interpolation='nearest')

    plt.xticks([])
    plt.yticks([])
    plt.title("Checkerboard Pattern", fontsize=14, fontweight='bold')

    plt.show()

plot_checkerboard(8)