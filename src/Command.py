
class Command():
    def __init__(self, command_str):
        self.arguments = self.process_input(command_str)
        self.command = self.process_command(command_str)


        # 'Static dictionary for the valid input classes inside the command given
        # In the future should be replaced by a database
        self.commands_dict = {'plot': ['FunctionManager']}
        self.input_types = self.commands_dict[self.command]
        self.input_object = []
        exec("self.input_objects.append({}({}))".format(self.input_types[0], self.arguments))

    def run(self):
        """
        """
        pass

    def process_input(self, command_str):
        output_str = command_str.strip()
        output_str = output_str.split("{")
        output_str = output_str[1]

        output_str= output_str[-1]
        return output_str

    def process_command(self, command_str):
        output_str = command_str.strip()
        output_str = output_str.split("{")
        output_str = output_str[0]
        output_str = output_str[1:]

        return output_str