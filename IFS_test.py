from IFS import IFS
from markovchain import Chain
from render_tools import render_points_to_array
import numpy as np
import matplotlib.pylab as plt
import os

if __name__ == "__main__":
    print("Running IFS tests for fractal rendering...")

    #sample plotting

    def f1(v):
        a,b,c,d,e,f = 0,0,0,0.16,0,0

        F = np.array([[a,b],[c,d]])
        C = np.array([e,f])

        return F @ np.array(v) + C

    def f2(v):
        a,b,c,d,e,f = 0.85,0.04,-0.04,0.85,0,1.6
        F = np.array([[a,b],[c,d]])
        C = np.array([e,f])
        return F @ np.array(v) + C
    def f3(v):
        a,b,c,d,e,f = 0.20, -0.26,0.23, 0.22, 0, 1.60
        F = np.array([[a,b],[c,d]])
        C = np.array([e,f])
        return F @ np.array(v) + C

    def f4(v):
        a,b,c,d,e,f = -0.15,0.28,0.26,0.24,0,0.44
        F = np.array([[a,b],[c,d]])
        C = np.array([e,f])
        return F @ np.array(v) + C

    funcs = [f1,f2,f3,f4]
    transitions =[ [0.02, 0.84, 0.07, 0.07],
                [0.02, 0.84, 0.07, 0.07],
                [0.02, 0.84, 0.07, 0.07],
                [0.02, 0.84, 0.07, 0.07]  ]

    start_state = f1
    start_time_init = os.times()[0]
    Barnsley_fern = IFS(funcs, transitions,start_state)
    end_time_init = os.times()[0]
    print("Initializing an IFS with functions took: {} seconds.".format(end_time_init- start_time_init))
    
    fig,ax = plt.subplots()
    extent = [-4,4,0,9]
    # breakpoint()
    start_time = os.times()[0]
    a = Barnsley_fern.render(200, start_state, 10)
    ## find max and min x,y values`
    end_time = os.times()[0]
    print("Simulating orbits of functions took: {} seconds".format(end_time - start_time))
    zs = np.zeros((300,300))

    start_time = os.times()[0]
    ready = render_points_to_array(a,zs,extent)
    end_time = os.times()[0]
    print("Computing points to a displayable numpy array took: {} seconds".format(end_time - start_time))

    start_time = os.times()[0]
    ax.imshow(ready, cmap = "viridis", extent = extent, origin = "lower")
    plt.show()
    end_time = os.times()[0]

    print("Displaying resulting fractal using matplotlib took: {} seconds".format(end_time - start_time))