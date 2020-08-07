import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from src.Function import Function

f = Function("f(x,y) = ((sin(x)*log(x)+pi)//1)")
print("Domain dimension is {}".format(f.in_dimension))
print("Co-Domain dimension is {}".format(f.out_dimension))

if f.in_dimension + f.out_dimension <= 2:
    xs = np.linspace(-1,1)
    ys = []

    for x in xs:
        ys.append(f.evaluate(x))
    ys = np.array(ys)

    fig, ax = plt.subplots()
    ax.plot(xs,ys)

elif f.in_dimension + f.out_dimension == 3:
    if f.in_dimension == 2:
        xs = np.arange(-5, 5, 0.25)
        ys = np.arange(-5, 5, 0.25)
        zs = []
        for i in range(len(xs)):
            zs.append(f.evaluate(xs[i],ys[i]))
        zs = np.array(zs)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.contour(xs, ys, zs, linewidth=0.2, antialiased=True)


    if f.out_dimension == 2:
        pass

plt.show()











# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, linewidth = 0)# cmap=cm.coolwarm,
#                        #linewidth=0, antialiased=False)
# # fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()