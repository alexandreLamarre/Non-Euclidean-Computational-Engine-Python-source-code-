import tkinter as tk
from GUI.PlotFrame import IFSPlotFrame
from src.CommandManager import CommandManager

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

class CLI(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self,*args,**kwargs)
        self.num_rows = 1
        self.CLI_text = None
        self.information = []
        self.add_command_line()


    def add_command_line(self):
        label = tk.Label(self, text = "Enter an expression to be computed", font = ("Times New Roman", 20) )
        label.grid(row = 0, column = 0)
        text = tk.StringVar(None)
        CLI = tk.Entry(self, textvariable = text, width = 70, font = ("Calibri", 14))
        CLI.grid(row = self.num_rows, column = 0,ipady=8)
        self.CLI_text = CLI
        bText = tk.StringVar()
        bText.set("=")
        CLI_button = tk.Button(self, textvariable = bText, command = self.run_command )
        CLI_button.grid(row = self.num_rows, column =1,)
        self.num_rows += 1


    def run_command(self):
        if self.information != []:
            for el in self.information:
                el.destroy()
        commands = CommandManager(self.CLI_text.get())
        interpreted = commands.get_interpreted()
        uninterpreted = commands.get_uninterpreted()

        label = tk.Label(self, text = interpreted, font = ("Calibri", 14))
        label2 = tk.Label(self, text = uninterpreted, fg="red", font = ("Calibri", 14))
        label.grid(row = self.num_rows, column = 0)
        label2.grid(row = self.num_rows, column = 0)

        self.information.append(label)
        self.information.append(label2)