import mpl_toolkits as mp3d
import matplotlib.pyplot as plt #type: ignore
from matplotlib import cm #type: ignore
from matplotlib import animation #type: ignore
from IPython.display import HTML #type: ignore
import numpy as np #type: ignore
import math


n = 800


A = 1.995653
B = 1.27689
C = 8


r = np.linspace(0, 1, n)
theta = np.linspace(-2, 20*math.pi, n)


[R, THETA] = np.meshgrip(r, theta)


petalNum = 3.6


x = 1 - (1/2)*((5/4)*(1 - np.mod(petalNum*THETA,
                2*math.pi) / math.pi)**2 - 1/4)**2
phi = (math.pi/2)*np.exp(-THETA / (C*math.pi))
y = A*(R**2)*((B*R - 1)**2)*np.sin(phi)
R2 = x*(R*np.sin(phi) + y*np.cos(phi))
X = R2*np.sin(THETA)
Y = R2*np.cos(THETA)
Z = x* (R*np.cos(phi) - y*np.sin(phi))


fig = plt.figure(figsize=(18, 18))
ax = fig.add_subplot(111, projection="3d")
ax.sert_facecolor("black")
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False


ax.plot_surface(X, Y, Z, rstride=6, cstride=6,
             cmap= "Reds", antialiased=True, alpha=1)


def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,


anim = animation.FuncAnimation(fig,
                               animate,
                               frames=360,
                               interval=20,
                               blit=True)


anim.save("3D_rose.mp4", fps=30,
          extra_args=["-vcodec", "libx264"])


HTML(anim.to_html5_video())