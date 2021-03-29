
import numpy as np


def make_instance():
    # [x, y, z] and [vx, vy, vz] and mass of particle 1
    pos1 = [0.5, 0.0, 0.0]
    vel1 = [0.0, 2.0, 0.0]
    mass1 = 1
    # [x, y, z] and [vx, vy, vz] of particle 2
    pos2 = [0.0, 0.0, 0.0]
    vel2 = [0.0, 0.0, 0.0]
    mass2 = 10
    # [x, y, z] and [vx, vy, vz] of particle 3
    pos3 = [-0.5, 0.0, 0.0]
    vel3 = [0.0, -2.0, 0.0]
    mass3 = 1
    # set num_t
    num_step = 1000
    dt = 1 / 1000
    # conver to numpy array
    pos = np.array([pos1, pos2, pos3])
    vel = np.array([vel1, vel2, vel3])
    mass = np.array([mass1, mass2, mass3])
    # compute momentum
    mom = np.array([mass[i] * vel[i] for i in range(len(pos))])
    return pos, mass, mom, num_step, dt


