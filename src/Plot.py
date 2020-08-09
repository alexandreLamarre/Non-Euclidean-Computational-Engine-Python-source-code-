from src.FunctionManager import FunctionManager
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from src.Function import Function
import os

class Plot:
    """
    Class responsible for plotting functions in Function Manager
    """
    def __init__(self, functionManager, N = 10000):
        self.functionManager = functionManager
        self.num_points = N

    def run(self):
        y_grid, x_grid = self.preprocess()
        start_time = os.times()[0]
        fig = plt.figure()
        gs = 0
        # gs = fig.add_gridspec(y_grid, x_grid)
        i = 1
        for f in self.functionManager.Functions_container:
            fig = plt.figure(i)
            if f.in_dimension == 1 and f.out_dimension == 1:
                self.plot2d(f, fig,gs, i, 0)
            elif f.in_dimension == 1 and f.out_dimension == 2:
                self.plot3d_one_two(f,fig,gs,i,0)
            elif f.in_dimension == 2 and f.out_dimension == 1:
                self.plot3d_two_one(f,fig,gs,i,0)
            i += 1
        end_time = os.times()[0]
        print("Plotting took: {} seconds".format(end_time - start_time))
        plt.rc('xtick', labelsize=8)
        plt.rc('ytick', labelsize=8)
        plt.show()

    def preprocess(self):
        y_grid = 1
        x_grid = 1
        for f in self.functionManager.Functions_container:
            y_grid += 1

        return y_grid, x_grid

    def plot2d(self,function, figure, grid, y_grid_number = 0, x_grid_number = 0):

        xs = np.linspace(-5, 5, self.num_points)
        ys = []

        for x in xs:
            ys.append(function.evaluate(x))
        ys = np.array(ys)

        ax = figure.add_subplot()#grid[y_grid_number:,:])
        ax.plot(xs,ys)
        ax.set_xlabel("{}".format(function.str_vars[0]), fontsize="8")
        ax.set_ylabel("{} = {}".format(function.name, function.str_funcs[0]), fontsize="8", rotation = "horizontal")


    def plot3d_two_one(self, function, figure,grid, y_grid = 0, x_grid = 0):
        xs = np.linspace(-5, 5, 200)
        ys = np.linspace(-5, 5, 200)

        zs = []
        for i in range(len(xs)):
            zs_row = []
            for j in range(len(ys)):
                value = function.evaluate(xs[i], ys[j])
                # print("the value is {}".format(value))
                if value != [None]:
                    zs_row += value
                else:
                    # print("Adding 0")
                    zs_row += [0]

            zs.append(zs_row)
        zs = np.array(zs)
        zs = np.nan_to_num(zs)
        xs, ys = np.meshgrid(xs, ys)
        ax = figure.add_subplot(projection = "3d")#grid[y_grid:, :], projection="3d")
        ax.plot_surface(xs, ys, zs, cmap=cm.get_cmap("Spectral"), antialiased=True)


    def plot3d_one_two(self, function, figure, grid, y_grid =0, x_grid = 0):
        xs = np.linspace(-5,5,4000)
        ys = []
        zs = []
        for i in range(xs.size):
            new_y, new_z = function.evaluate(xs[i])
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
        xs, ys = np.meshgrid(xs, ys)
        copy_xs, zs = np.meshgrid(copy_xs, zs)


        ax = figure.add_subplot(projection = "3d")#grid[y_grid,x_grid], projection="3d")
        ax.plot_surface(xs,ys,zs, cmap = cm.get_cmap("Spectral"), antialiased = True)

if __name__ == "__main__":
    fm = FunctionManager("f(x,y) = (x**2 + 1/y) g(y) = (y**2, y**3) f(k) = (log(k))")
    p = Plot(fm)
    p.run()