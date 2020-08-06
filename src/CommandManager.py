from interpreter import CommandInterpreter
from Command import Command


class CommandManager(CommandInterpreter):

    def __init__(self, commands_str):
        """"""
        super().__init__()
        self.command_str_container = self.match(commands_str)
        self.uninterpreted = self.process_uninterpreted(commands_str)
        self.Commands_container = [Command(c) for c in self.command_str_container]


    def run_all(self):
        for c in self.Commands_container:
            c.run()

    def run_default(self):
        #plot, zeroes, derivative, factorization, integral?
        pass


    def process_uninterpreted(self, in_str):
        res = in_str
        for cstr in self.command_str_container:
            assert (cstr in res), "Interpreted input was not even in the input to begin with??"
            start_index = res.find(cstr)
            end_index = start_index + len(cstr)
            res = res[0:start_index] + "\n" + res[end_index:]
            res.strip()
        return res

    def get_interpreted(self):
        output_message = ""
        for c in self.command_str_container:
            output_message += c.strip() + "..." +'\n'

        return "Running: \n" + output_message if output_message else ""



    def get_uninterpreted(self):
        output_message = self.uninterpreted.strip()
        return "Could not interpret the following as commands :\n" + output_message if output_message else ""

    def generate_reason_uninterpreted(self, failed_str):
        pass

if __name__ == "__main__":

    c = CommandManager("\plotf(x) = (x**2)}")
    print(c.get_interpreted())
    print(c.get_uninterpreted())