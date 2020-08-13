import tkinter as tk

class InputFrame(tk.Frame):
    def __init__(self, embedded, main_label, sub_labels_and_info):
        tk.Frame.__init__(self, embedded)
        self.main_label = main_label
        self.sub_labels_and_info = sub_labels_and_info
        self.num_rows = 0
        self.add_layout()

    def add_layout(self):
        MainLabelText = tk.StringVar()
        MainLabelText.set(self.main_label)
        MainLabel = tk.Label(self, textvariable = MainLabelText, background = "AntiqueWhite3", anchor = "w", width = 110)
        MainLabel.grid(row = self.num_rows, sticky = "ew")
        self.num_rows += 1

        sub_labels = [el[0] for el in self.sub_labels_and_info]

        no_repeat_sublabels = []
        for el in sub_labels:
            if el not in no_repeat_sublabels:
                no_repeat_sublabels.append(el)

        for sublabel in no_repeat_sublabels:
            SubLabelText = tk.StringVar()
            SubLabelText.set(sublabel)
            SubLabel = tk.Label(self, textvariable = SubLabelText, background = "AntiqueWhite2", anchor = "w")

            sublabel_info_text = ""

            for sublabel_info in self.sub_labels_and_info:
                if sublabel_info[0] == sublabel:
                    if sublabel_info[1] != None:
                        sublabel_info_text += sublabel_info[1]
            print(sublabel_info_text)
            sublabel_info_text = "None" if sublabel_info_text == "" else sublabel_info_text
            SubLabelInfoText = tk.StringVar()
            SubLabelInfoText.set(sublabel_info_text)
            SubLabelInfo = tk.Label(self, textvariable = SubLabelInfoText, background = "AntiqueWhite1", anchor = "w")
            SubLabel.grid(row = self.num_rows, column = 0,sticky = "ew")
            self.num_rows += 1
            SubLabelInfo.grid(row = self.num_rows, column = 0,sticky = "ew")
            self.num_rows += 1