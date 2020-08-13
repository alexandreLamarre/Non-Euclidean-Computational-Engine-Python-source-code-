import tkinter as tk

class InfoFrame(tk.Frame):
    def __init__(self, main_label, sub_labels):
        tk.Frame.__init__(self)
        self.main_label = main_label
        self.sub_labels = sub_labels
        self.num_rows = 0

    def add_layout(self):
        mainLabelText = tk.StringVar("")
        mainLabelText.set(self.main_label)
        mainLabel = tk.Label(self, textvariable = mainLabelText)
        mainLabel.grid(row = self.num_rows, column = 0)
        self.num_rows += 1
        for i in self.sub_labels:
            newTextVariable = tk.StringVar("")
            newTextVariable.set(i)
            subLabel = tk.Label(self, textvariable = newTextVariable)
            subLabel.grid(row = self.num_rows, column = 0)
            self.num_rows += 2

    def set_info_frame(self, sub_label, frame):
        """
        Takes a string which is the name of the sub label to add info to
        Takes a frame and grids it to the info frame
        """
        for i in range(len(self.sub_labels)):
            if sub_label == sub_label[i]:
                frame.grid(row = [2*i+2], column = 0)
