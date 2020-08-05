import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.render_tools import plot_IFS

class IFSPlotFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


    def mat_plot_canvas(self, functions, transitions):
        figure = plot_IFS(functions, transitions)
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack()