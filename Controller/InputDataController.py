import queue
from src.CommandManager import CommandManager

class InputDataController:
    def __init__(self):
        self.queue = queue.Queue()
        self.command_manager = None

    def set_commands(self, CommandLineString):
        new_command_manager = CommandManager(CommandLineString)

        self.command_manager = new_command_manager

    def run_commands(self):
        if self.command_manager.initial_done == True:
            label, sublabels_and_frame_info_tuple = self.command_manager.run_next()

            self.queue.put([label, sublabels_and_frame_info_tuple])
        else:
            label, sublabels_and_frame_info_tuple = self.command_manager.run_initial()

            self.queue.put([label, sublabels_and_frame_info_tuple])

if __name__ == "__main__":
    new_input_controller = InputDataController()
