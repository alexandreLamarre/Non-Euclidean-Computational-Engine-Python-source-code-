import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.render_tools import plot_IFS

class PlotFrame(tk.Frame):
    def __init__(self, functions, transitions):
        tk.Frame.__init__(self)
        self.mat_plot_canvas(functions, transitions)

    def mat_plot_canvas(self, functions, transitions):
        figure = plot_IFS(functions, transitions)
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack()