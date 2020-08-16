import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.render_tools import plot_IFS
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from io import BytesIO
import sympy as sp


class PlotFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)


    def mat_plot_canvas(self, figure):
        canvas = FigureCanvasTkAgg(figure, self)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def mat_latex_canvas(self, text):
        print("In latex canvas, text is {}".format(text))
        # plt.rc('text', usetex=True)
        # plt.rc('font', family='serif')
        # # plt.plot(1, 1)
        # # plt.title(r"{}".format(text),
        # #           fontsize=16, color='gray')
        # figure = plt.figure()
        # ax = figure.add_subplot()
        # ax.get_xaxis().set_visible(False)
        # ax.get_yaxis().set_visible(False)
        # ax.text(0.1, 0.1, text, fontsize = 10)
        # canvas = FigureCanvasTkAgg(figure, self)
        # canvas.draw()
        # canvas.get_tk_widget().grid(row = 0, column = 0)
        text = "$\displaystyle " + text + "$"

        # This creates a ByteIO stream and saves there the output of sympy.preview
        f = BytesIO()
        the_color = "{" + self.master.cget('bg')[1:].upper() + "}"
        sp.preview(text, euler=False, preamble=r"\documentclass{standalone}"
                                               r"\usepackage{pagecolor}"
                                               r"\definecolor{graybg}{HTML}" + the_color +
                                               r"\pagecolor{graybg}"
                                               r"\begin{document}",
                   viewer="BytesIO", output="ps", outputbuffer=f)
        f.seek(0)
        # Open the image as if it were a file. This works only for .ps!
        img = Image.open(f)
        # See note at the bottom
        img.load(scale=10)
        img = img.resize((int(img.size[0] / 2), int(img.size[1] / 2)), Image.BILINEAR)
        photo = ImageTk.PhotoImage(img)
        newLabel = tk.Label(self)
        newLabel.config(image=photo)
        newLabel.grid(row = 0, column = 0)
        f.close()