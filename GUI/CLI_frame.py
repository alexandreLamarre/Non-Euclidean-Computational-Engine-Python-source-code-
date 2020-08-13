import tkinter as tk
from GUI.PlotFrame import PlotFrame
from src.CommandManager import CommandManager
from GUI.ScrollableFrame import ScrollableFrame
from Controller.InputDataController import InputDataController
from GUI.InfoFrame import InfoFrame
from GUI.InputFrame import InputFrame
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

class CLI(ScrollableFrame):
    def __init__(self,parent):
        ScrollableFrame.__init__(self,parent)

        self.controller = InputDataController()
        self.num_rows = 1
        self.CLI_text = None
        self.information = []
        self.processing_data = False
        self.refresher()
        self.add_command_line()


    def add_command_line(self):
        label = tk.Label(self.frame, text = "Enter an expression to be computed", font = ("Latin Modern", 20), background = "AntiqueWhite1" )
        label.grid(row = 0, column = 0, sticky = "EW")
        text = tk.StringVar(None)
        CLI = tk.Entry(self.frame, textvariable = text, width = 75, font = ("Calibri", 14))
        CLI.grid(row = self.num_rows, column = 0,ipady=8, sticky = "EW")
        self.CLI_text = CLI
        bText = tk.StringVar()
        bText.set("=")
        CLI_button = tk.Button(self.frame, textvariable = bText, command = self.on_click )
        CLI_button.grid(row = self.num_rows, column =1, sticky = "EW")
        self.num_rows += 1

    def on_click(self):
        if self.information != []:
            for el in self.information:
                el.destroy()
        command_string = self.CLI_text.get()
        self.controller.set_commands(command_string)
        self.processing_data = True

    def refresher(self):
        self.after(200, self.refresher)
        if self.controller.queue.empty():
            pass
        else:
            print("Data Queue has something")
            self.create_new_info_frame()
        if self.processing_data == True:
            self.controller.run_commands()
            self.processing_data = False

    def create_new_info_frame(self):
        main_label, sublabels_and_info = self.controller.queue.get()
        print(main_label)
        print(sublabels_and_info)
        if main_label == "Input":
            new_frame = InputFrame(self.frame, main_label, sublabels_and_info)
            new_frame.grid(row=self.num_rows, column=0, sticky="W")
            self.num_rows += 1
            self.information.append(new_frame)

    # def run_command(self):
    #     if self.information != []:
    #         for el in self.information:
    #             el.destroy()
    #     commands = CommandManager(self.CLI_text.get())
    #     interpreted = commands.get_interpreted()
    #     uninterpreted = commands.get_uninterpreted()
    #
    #     label = tk.Label(self.frame, text = interpreted, font = ("Calibri", 14))
    #     label2 = tk.Label(self.frame, text = uninterpreted, fg="red", font = ("Calibri", 14))
    #     label.grid(row = self.num_rows, column = 0, sticky = "W")
    #     self.num_rows += 1
    #     label2.grid(row = self.num_rows, column = 0, sticky ="W")
    #     self.num_rows += 1
    #
    #     self.information.append(label)
    #     self.information.append(label2)
    #     ## assuming no stop execs continue:
    #     self.process_commands(commands)
    #
    # def process_commands(self, commands):
    #     for el in commands.Commands_container:
    #         ## assumes plotting command
    #         output = el.run()
    #         for plot in output:
    #             plot_frame = PlotFrame(self.frame)
    #             self.information.append(plot_frame)
    #             plot_frame.mat_plot_canvas(plot)
    #             plot_frame.grid(row = self.num_rows, column = 0)
    #             self.num_rows += 1