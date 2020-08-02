import numpy as np
from src.render_tools import plot_IFS

if __name__ == "__main__":
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

    figure = plot_IFS(funcs,transitions)
    figure.show()