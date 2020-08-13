import tkinter as tk
from GUI.PlotFrame import PlotFrame

class InputPlotFrame(tk.Frame):
    def __init__(self, embedded, main_label, sub_labels_and_info):
        tk.Frame.__init__(self, embedded)
        self.main_label = main_label
        self.sub_labels_and_info = sub_labels_and_info
        self.num_rows = 0
        self.add_layout()

    def add_layout(self):
        MainLabelText = tk.StringVar()
        MainLabelText.set(self.main_label)
        MainLabel = tk.Label(self, textvariable=MainLabelText, background="AntiqueWhite3", anchor="w", width=110)
        MainLabel.grid(row=self.num_rows, sticky="ew")
        self.num_rows += 1

        for el in self.sub_labels_and_info:
            new_plot = PlotFrame(self, background = "AntiqueWhite1")
            new_plot.mat_plot_canvas(el[1])
            new_plot.grid(row = self.num_rows)
            self.num_rows += 1