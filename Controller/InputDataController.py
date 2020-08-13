import queue
from src.CommandManager import CommandManager
class InputDataController():

    def __init__(self):
        self.queue = queue.Queue()

    def add_commands(self, CommandLineString):
        new_command_manager = CommandManager(CommandLineString)


