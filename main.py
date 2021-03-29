
import matplotlib.pyplot as plt
import matplotlib.animation as anm

import make_instance as mi
import runge_kutta as rk


if __name__ == '__main__':
    pos, mass, mom, num_step, dt = mi.make_instance()
    fig = plt.figure()
    ims = []
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    colors = ['r', 'g', 'b']
    for i in range(1000):
        pos, mom = rk.runge_kutta_4th(pos, mass, mom, dt)
        im = plt.plot(pos[0][0], pos[0][1], marker='.', color=colors[0], markersize=mass[0]*5)
        for j in range(1, len(pos)):
            im += plt.plot(pos[j][0], pos[j][1], marker='.', color=colors[j], markersize=mass[j]*5)
        ims.append(im)
    ani = anm.ArtistAnimation(fig, ims, interval=1)
    plt.show()