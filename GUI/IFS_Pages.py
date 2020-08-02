import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

class IFSPage1(Page):
    """ Page for 3-dimensional IFS using vars (x,y,z)"""
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.add_layout()

    def add_layout(self):
        label = tk.Label(self, text = "This is a 3-Dimensional IFS Fractal Computation")
        label.pack(side = "top", expand = True)

class IFSPage2(Page):
    """ Layout for IFS using custom vars"""
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.add_layout()

    def add_layout(self):
        label = tk.Label(self, text = "This is a custom n-Dimensional IFS Fractal Computation")
        label.pack(side = "top", expand = True)
