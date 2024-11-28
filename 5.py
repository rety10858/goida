from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
t = 10

def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * 16 * (np.sin(alpha)**3)
    y = R * 13 * np.cos(alpha) - 5 * np.cos(alpha * 2) - 2 * np.cos(alpha * 3) - np.cos(alpha * 4)
    return x, y
 
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')
 
frames = 1100
coords = np.zeros((frames, 2))
 
 
def animate(i):
    coords[i] = circle_move(R=2, angle_vel=1, time=i)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('animation_2.gif', writer="pillow")