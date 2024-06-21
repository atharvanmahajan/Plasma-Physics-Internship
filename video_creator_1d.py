# video_creator.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib

def create_video(grid, filename, x_lim=(-50, 50)):
    matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive plotting

    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(x_lim[0], x_lim[1])
    ax.set_ylim(np.min(grid), np.max(grid))

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        x = np.linspace(x_lim[0], x_lim[1], len(grid[i]))
        y = grid[i]
        line.set_data(x, y)
        return line,

    ani = FuncAnimation(fig, animate, init_func=init, frames=len(grid), interval=50, blit=True)
    ani.save(filename, writer='ffmpeg')