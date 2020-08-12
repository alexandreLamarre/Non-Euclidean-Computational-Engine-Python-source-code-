from src.interpreter import CommandInterpreter
from src.Command import Command


class CommandManager(CommandInterpreter):
    """ Factory object that processes the command line input
    And instantiates the commands to be run at runtime depending on their specifications

    Implements an Interpreter interface because it processes user input"""

    def __init__(self, commands_str):
        """
        None -> None

        Instantiates a new CommandManager Object

        Interprets the commands as acceptable/unnaceptable using the Interpreter interface
        Creates a list of Command Objects using those strings
        """
        super().__init__()
        self.command_str_container = self.match(commands_str)
        self.uninterpreted = self.process_uninterpreted(commands_str)
        self.Commands_container = [Command(c) for c in self.command_str_container]


    def run_all(self):
        """
        None -> #TODO

        Runs all commands interpreted by the command manager
        """
        for c in self.Commands_container:
            c.run()

    def run_default(self):
        """
        None -> #TODO

        When no commands are specified in the command line, run default commands.
        """
        #plot, zeroes, derivative, factorization, integral?
        pass


    def process_uninterpreted(self, in_str):
        """
        (String) -> (String)

        Processes uninterpreted strings entered in the command line
        by removing the intrepretable input and separating the resulting strings

        Returns a string representing uninterpreted output
        """
        res = in_str
        for cstr in self.command_str_container:
            assert (cstr in res), "Interpreted input was not even in the input to begin with??"
            start_index = res.find(cstr)
            end_index = start_index + len(cstr)
            res = res[0:start_index] + "\n" + res[end_index:]
            res.strip()
        return res

    def get_interpreted(self):
        """
        (None) -> (String)

        Returns the interpreted commands (matched to regex by interpreter interface) in the command line
        formatted to a user friendly string.
        """
        output_message = ""
        for c in self.Commands_container:
            output_message += "Running " + c.get_command_name() + "...\n" +c.get_math_object_information() + "\n"

        return output_message if output_message else ""


    def get_uninterpreted(self):
        """
        (None) -> String

        Returns the uninterpreted commands in the command line formatted to a user friendly string
        """
        output_message = self.uninterpreted.strip()
        return "Could not interpret the following as commands :\n" + output_message if output_message else ""



if __name__ == "__main__":

    c = CommandManager("\plot{f(x) = (x**2)} \plot{laplace(x,y,z) = (x** (1/3), y**(1/3), z**(1/3)) fourrier(x) = (x^5)}")
    print(c.get_interpreted())
    print(c.get_uninterpreted())
    x = 5
    print(x^5)