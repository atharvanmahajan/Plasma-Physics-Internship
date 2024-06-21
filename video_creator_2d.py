# video_creator.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

def create_video(grid, filename):
    matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive plotting

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, grid.shape[2] - 1)
    ax.set_ylim(0, grid.shape[1] - 1)

    contour = None

    def init():
        nonlocal contour
        contour = ax.contourf(grid[0, :, :], levels=20, cmap='viridis')
        return contour.collections

    def animate(i):
        nonlocal contour
        for c in contour.collections:
            c.remove()
        contour = ax.contourf(grid[i, :, :], levels=20, cmap='viridis')
        return contour.collections

    ani = FuncAnimation(fig, animate, init_func=init, frames=len(grid), interval=50, blit=True)
    ani.save(filename, writer='ffmpeg')