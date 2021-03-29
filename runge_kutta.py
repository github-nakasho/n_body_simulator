
import numpy as np


def function_for_pos(mass, mom):
    return mom / mass

def function_for_mom(mass1, mass2, diff, dist):
    return - mass1 * mass2 / dist ** 3 * diff

def compute_k(mass, pos, mom):
    pos_k = [0] * len(pos)
    mom_k = [0] * len(pos)
    tmp_index = np.arange(len(pos))
    index_j, index_i = np.meshgrid(tmp_index, tmp_index)
    for i in range(len(pos)):    
        diff = pos[index_i] - pos[index_j]
        dist = np.linalg.norm(pos[index_i]-pos[index_j], axis=2)
        pos_k[i] = function_for_pos(mass[i], mom[i])
        mom_k[i] = np.nansum([function_for_mom(mass[i], mass[j], diff[i][j], dist[i][j]) for j in range(len(pos))], axis=0)
    return np.array(pos_k), np.array(mom_k)

def runge_kutta_4th(pos, mass, mom, dt):
    pos_k1, mom_k1 = compute_k(mass, pos, mom)
    tmp_pos = pos + 0.5 * dt * pos_k1
    tmp_mom = mom + 0.5 * dt * mom_k1    
    pos_k2, mom_k2 = compute_k(mass, tmp_pos, tmp_mom)
    tmp_pos = pos + 0.5 * dt * pos_k2
    tmp_mom = mom + 0.5 * dt * mom_k2
    pos_k3, mom_k3 = compute_k(mass, tmp_pos, tmp_mom)
    tmp_pos = pos + dt * np.array(pos_k3)
    tmp_mom = mom + dt * np.array(mom_k3)
    pos_k4, mom_k4 = compute_k(mass, tmp_pos, tmp_mom)
        
    delta_pos = dt / 6 * (pos_k1+2*pos_k2+2*pos_k3+pos_k4)
    delta_mom = dt / 6 * (mom_k1+2*mom_k2+2*mom_k3+mom_k4)
        
    pos = pos + delta_pos
    mom = mom + delta_mom

    return pos, mom


