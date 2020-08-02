import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PlotFrame(tk.Frame):
    def __init__(self, functions, transitions):
        tk.Frame.__init__(self)

    def mat_plot_canvas(self):
        # figure = IFS_plot()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()