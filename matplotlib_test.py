import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from src.Function import Function
import os

f = Function("f(x) = (sin(x), x**2)")
print("Domain dimension is {}".format(f.in_dimension))
print("Co-Domain dimension is {}".format(f.out_dimension))

if f.in_dimension + f.out_dimension <= 2:
    xs = np.linspace(-19,19,10000)
    ys = []

    for x in xs:
        ys.append(f.evaluate(x))
    ys = np.array(ys)

    fig, ax = plt.subplots()
    ax.plot(xs,ys)
    plt.xlabel("{}".format(f.str_vars[0]), fontsize = "15")
    plt.ylabel("{} = {}".format(f.name, f.str_funcs[0]), fontsize = "15")



elif f.in_dimension + f.out_dimension == 3:
    print("hello")

    if f.in_dimension == 2:
        xs = np.linspace(-20,20,300)
        ys = np.linspace(-20,20,300)

        zs = []
        for i in range(len(xs)):
            zs_row = []
            for j in range(len(ys)):
                value = f.evaluate(xs[i], ys[j])
                # print("the value is {}".format(value))
                if value != [None]:
                    zs_row += value
                else:
                    # print("Adding 0")
                    zs_row += [0]

            zs.append(zs_row)
        zs = np.array(zs)
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
        ax.plot_surface(xs,ys,zs, linewidth=0.2, antialiased=True, cmap = cm.get_cmap("Spectral"))


    if f.out_dimension == 2:
        xs = np.linspace(-10,10,4000)

        ys = []
        zs = []
        for i in range(xs.size):
            new_y, new_z = f.evaluate(xs[i])
            if new_y != None:
                ys.append(new_y)
            else:
                ys.append(0)
            if new_z != None:
                zs.append(new_z)
            else:
                zs.append(0)

        ys = np.array(ys)
        zs = np.array(zs)
        copy_xs = xs
        xs,ys = np.meshgrid(xs,ys)
        copy_xs, zs = np.meshgrid(copy_xs, zs)


        fig = plt.figure()


        gs = fig.add_gridspec(1, 2)
        ax = fig.add_subplot(gs[0,0], projection='3d')

        # fig.gca(projection='3d')
        surf = ax.plot_surface(xs, ys, zs, linewidth=0.2, antialiased=True, cmap = cm.get_cmap("Spectral"))



        ax = fig.add_subplot(gs[0,1], projection = "3d")
        ax.plot_surface(xs,ys,zs)


plt.show()



