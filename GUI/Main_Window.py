import tkinter as tk
from tkinter import ttk

class Main_Window(tk.Tk):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.title("NE Computational Engine")
        self.minsize(1000, 600)

        self.create_menu()

    def process_new(self):
        self.label = ttk.Label(self, text="Tkinter Application")
        self.label.grid(row = 0, column = 0)

    def create_menu(self):
        #Main menu
        menuBar = tk.Menu(self)
        self.config(menu = menuBar)
        #Menu/file/...
        file_menu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label = "File", menu = file_menu)
        #Menu/file/new/...
        new_menu = tk.Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label = "New", menu = new_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as")
        #Menu/file/new/IFS
        IFS_menu = tk.Menu(new_menu, tearoff = 0)
        new_menu.add_cascade(label = "Iterated Function Systems", menu = IFS_menu)
        IFS_menu.add_command(label = "3-Dimensional")
        IFS_menu.add_command(label = "Custom")
        #Menu/help
        help_menu = tk.Menu(menuBar, tearoff = 0)
        menuBar.add_cascade(label = "Help", menu = help_menu)
        help_menu.add_command(label = "About")


if __name__ == "__main__":
    window = Main_Window()
    window.mainloop()