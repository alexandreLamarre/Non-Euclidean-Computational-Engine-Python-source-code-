import numpy as np
import matplotlib.pylab as plt
from src.IFS import IFS

def render_points_to_array(points, array, extent, additive=False):
    array = array.copy()

    h, w = array.shape

    for p in points:
        x = np.clip(int((p[0] - extent[0]) / (extent[1] - extent[0])*w), 0, w-1)
        y = np.clip(int((p[1] - extent[2]) / (extent[3] - extent[2]) * h), 0, h-1)

        if additive:
            array[y][x] += 1
        else:
            array[y][x] = 1

    return array

def plot_IFS(functions, transitions):
    """ Return a matplot of an IFS figure, given a list of function and list of list transitions"""

    start_state = functions[0]
    fig,ax = plt.subplots()

    ifs_obj = IFS(functions, transitions, start_state)
    N = 150
    ifs_rendered = ifs_obj.render(N,start_state,10)

    zs = np.zeros((N,N))
    extent = create_extent(ifs_rendered)

    plottable_list= render_points_to_array(ifs_rendered, zs, extent)

    ax.imshow(plottable_list, cmap = "viridis", extent = extent)

    return plt.figure(1)

def create_extent(array):
    """ Creates an extent based on min, max values of each coordinate of a point  in a
    np array containing points (x,y,z)"""
    return [-2.5,2.5,0,9]
