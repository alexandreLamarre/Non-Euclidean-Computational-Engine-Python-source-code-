import tkinter as tk

class InfoFrame(tk.Frame):
    def __init__(self, embedded, main_label, sub_labels):
        tk.Frame.__init__(self, embedded)
        self.main_label = main_label
        self.sub_labels = sub_labels
        self.num_rows = 0
        self.add_layout()

    def add_layout(self):
        mainLabelText = tk.StringVar("")
        mainLabelText.set(self.main_label)
        mainLabel = tk.Label(self, textvariable = mainLabelText)
        mainLabel.grid(row = self.num_rows, column = 0, sticky = 'W')
        self.num_rows += 1
        for i in self.sub_labels:
            newTextVariable = tk.StringVar("")
            newTextVariable.set("\t"+ i )
            subLabel = tk.Label(self, textvariable = newTextVariable)
            subLabel.grid(row = self.num_rows, column = 0, sticky = "W")
            self.num_rows += 2

    def get_row(self, sub_label):
        """
        Takes a string which is the name of the sub label to add info to
        Takes a frame and grids it to the info frame
        """
        for i in range(len(self.sub_labels)):
            if sub_label == sub_label[i]:
                return i

    def process_info(self,info):
        if self.main_label =="Input":
            for i in range(len(info)):
                newText = tk.StringVar()
                if info[i][1] != None:
                    newText.set("\t"+info[i][1])
                else:
                    newText.set("None")
                newLabel= tk.Label(self, textvariable = newText, background="#ffffff")
                row_num = self.get_row(info[i][0])
                newLabel.grid(row = row_num, column = 0, sticky = "W")


        if self.main_label == "Plot":
            pass