import tkinter as tk
from tkinter import ttk
from GUI.ScrollableFrame import ScrollableFrame
# from GUI.IFS_Pages import IFSPage3d
# from GUI.IFS_Pages import IFSPage2
# from GUI.IFS.IFS_Frame import IFS_Frame
from GUI.CLI_frame import CLI
class Main_Window(tk.Tk):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.title("NE Computational Engine")

        self.minsize(800, 600)
        self.pages = []
        # self.create_menu()

        self.display_CLI()

    def clear_window(self):
        """ Clears windows of displayed Frames"""
        for p in self.pages:
            p.destroy()

    def add_to_window(self, p):
        """ Adds information/ frames to the window"""
        self.pages.append(p)

    def display_CLI(self):
        self.clear_window()
        p = CLI(self)
        self.add_to_window(p)
        p.pack()
    # def display_IFS_3D(self):
    #     self.clear_window()
    #     p = IFS_Frame(self)
    #     self.add_to_window(p)
    #     p.pack()
    #
    #
    #
    # def display_IFS_custom(self):
    #     self.clear_window()
    #     p = IFSPage2(self)
    #     self.add_to_window(p)
    #     p.pack()

    # def create_menu(self):
    #     #Main menu
    #     menuBar = tk.Menu(self)
    #     self.config(menu = menuBar)
    #     #Menu/file/...
    #     file_menu = tk.Menu(menuBar, tearoff=0)
    #     menuBar.add_cascade(label = "File", menu = file_menu)
    #     #Menu/file/new/...
    #     new_menu = tk.Menu(file_menu, tearoff=0)
    #     file_menu.add_cascade(label = "New", menu = new_menu)
    #     file_menu.add_separator()
    #     file_menu.add_command(label="Open")
    #     file_menu.add_command(label="Save")
    #     file_menu.add_command(label="Save as")
    #     #Menu/file/new/IFS
    #     IFS_menu = tk.Menu(new_menu, tearoff = 0)
    #     new_menu.add_cascade(label = "Iterated Function Systems", menu = IFS_menu)
    #     IFS_menu.add_command(label = "3-Dimensional", command = self.display_IFS_3D)
    #     IFS_menu.add_command(label = "Custom", command = self.display_IFS_custom)
    #     #Menu/help
    #     help_menu = tk.Menu(menuBar, tearoff = 0)
    #     menuBar.add_cascade(label = "Help", menu = help_menu)
    #     help_menu.add_command(label = "About")


if __name__ == "__main__":
    window = Main_Window()
    window.mainloop()