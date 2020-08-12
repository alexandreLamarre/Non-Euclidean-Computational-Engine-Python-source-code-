import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.render_tools import plot_IFS

class PlotFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


    def mat_plot_canvas(self, figure):
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack()