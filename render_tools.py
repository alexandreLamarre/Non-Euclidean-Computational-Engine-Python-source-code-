import numpy as np

def render_points_to_array(points, array, extent, additive = False):
    array = array.copy()

    h,w = array.shape

    for p in points:
        x = np.clip( int((p[0] - extent[0])/ (extent[1] - extent[0])* w ), 0, w-1 )
        y = np.clip( int((p[1] - extent[2]) / (extent[3] - extent[2]) * h), 0, h -1)

        if additive:
            array[y][x] += 1
        else:
            array[y][x] = 1

    return array

# fig,ax = plt.subplots()
##ax.imshow(Usage render_points_to_array(l, zs, extent), cmap = "viridis", extent= extent))
#plt.show
