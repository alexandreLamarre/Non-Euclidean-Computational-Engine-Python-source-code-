import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from src.Function import Function

f = Function("f(x,y) = ((x^2+y^2)^(1/2))")
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
    ax.legend([f.name])



elif f.in_dimension + f.out_dimension == 3:
    if f.in_dimension == 2:
        xs = np.linspace(-1,1,100)
        ys = np.linspace(-1,1,100)

        def g(x,y):
            return f.evaluate(x,y)
        #g(x,y) = f.evaluate(x,y)
        # def g(x,y):
        #     return np.sqrt(x**2+y**2)
        #
        # g = np.vectorize(f.get_codomain_functions()[0])
        zs = []
        for i in range(len(xs)):
            zs_row = []
            for j in range(len(ys)):
                value = f.evaluate(xs[i], ys[j])
                print("the value is {}".format(value))
                if value != [None]:
                    zs_row += value
                else:
                    print("Adding 0")
                    zs_row += [0]

            zs.append(zs_row)
        zs = np.array(zs)
        print(np.array(np.nan))
        zs = np.nan_to_num(zs)

        xs,ys = np.meshgrid(xs,ys)




        # zs = g(xs,ys)
        # for i in range(len(xs)):
        #     for j in range(len(ys)):
        #         new_list = []
        #         for i2 in range(len(xs)):
        #             for j2 in range(len(ys)):
        #                 new_list.append(f.evaluate(xs[i][i2], ys[j][j2]))
        #         zs.append(np.array(new_list))
        # zs = np.array(zs)
        print("Xs")
        print(xs)
        print("Ys")
        print(ys)
        print("Zs")
        print(zs)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.legend([f.name, "", ""])
        ax.plot_surface(xs,ys,zs)


    if f.out_dimension == 2:
        pass

plt.show()











# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# print(X)
# print(Y)
# X, Y = np.meshgrid(X, Y)
# print(X)
# print(Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, linewidth = 0)# cmap=cm.coolwarm,
#                        #linewidth=0, antialiased=False)
# # fig.colorbar(surf, shrink=0.5, aspect=5)
#
# plt.show()