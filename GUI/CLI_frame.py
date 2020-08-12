import tkinter as tk
from GUI.PlotFrame import PlotFrame
from src.CommandManager import CommandManager
from GUI.ScrollableFrame import ScrollableFrame
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

class CLI(ScrollableFrame):
    def __init__(self,parent):
        ScrollableFrame.__init__(self,parent)


        self.num_rows = 1
        self.CLI_text = None
        self.information = []
        self.add_command_line()


    def add_command_line(self):
        label = tk.Label(self.frame, text = "Enter an expression to be computed", font = ("Times New Roman", 20) )
        label.grid(row = 0, column = 0, sticky = "W")
        text = tk.StringVar(None)
        CLI = tk.Entry(self.frame, textvariable = text, width = 75, font = ("Calibri", 14))
        CLI.grid(row = self.num_rows, column = 0,ipady=8)
        self.CLI_text = CLI
        bText = tk.StringVar()
        bText.set("=")
        CLI_button = tk.Button(self.frame, textvariable = bText, command = self.run_command )
        CLI_button.grid(row = self.num_rows, column =1,)
        self.num_rows += 1


    def run_command(self):
        if self.information != []:
            for el in self.information:
                el.destroy()
        commands = CommandManager(self.CLI_text.get())
        interpreted = commands.get_interpreted()
        uninterpreted = commands.get_uninterpreted()

        label = tk.Label(self.frame, text = interpreted, font = ("Calibri", 14))
        label2 = tk.Label(self.frame, text = uninterpreted, fg="red", font = ("Calibri", 14))
        label.grid(row = self.num_rows, column = 0, sticky = "W")
        self.num_rows += 1
        label2.grid(row = self.num_rows, column = 0, sticky ="W")
        self.num_rows += 1

        self.information.append(label)
        self.information.append(label2)
        ## assuming no stop execs continue:
        self.process_commands(commands)

    def process_commands(self, commands):
        for el in commands.Commands_container:
            ## assumes plotting command
            output = el.run()
            for plot in output:
                plot_frame = PlotFrame(self.frame)
                self.information.append(plot_frame)
                plot_frame.mat_plot_canvas(plot)
                plot_frame.grid(row = self.num_rows, column = 0)
                self.num_rows += 1