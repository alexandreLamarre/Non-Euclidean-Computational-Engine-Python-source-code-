from FunctionManager import FunctionManager

class Command():
    def __init__(self, command_str):
        self.arguments = self.process_input(command_str)
        self.command = self.process_command(command_str)


        # 'Static dictionary for the valid input classes inside the command given
        # In the future should be replaced by a database
        self.commands_dict = {'plot': ['FunctionManager'], 'IFS': ['FunctionManager', 'MarkovChain']}
        self.input_types = []

        assert(self.command in self.commands_dict), "Command not recognized"
        self.math_types = self.commands_dict[self.command]

        self.math_objects = self.process_input_types()

    def run(self):
        """
        """
        pass

    def process_input(self, command_str):
        output_str = command_str.strip()
        output_str = output_str.split("{")
        output_str = output_str[1]

        output_str= output_str[:-1]
        return output_str

    def process_command(self, command_str):
        output_str = command_str.strip()
        output_str = output_str.split("{")
        output_str = output_str[0]
        output_str = output_str[1:]

        return output_str

    def process_input_types(self):
        output_list = []
        for i in self.math_types:
            if i == "FunctionManager":
                    output_list.append(FunctionManager(self.arguments))
        return output_list

    def get_math_object_information(self):
        res = ""

        for obj in self.math_objects:
            res += obj.get_interpreted()

        res += "\n"

        for obj in self.math_objects:
            res += obj.get_uninterpreted()
            # res += obj.c

        for obj in self.math_objects:
            res += obj.get_compile_errors()


        return res

    def get_command_name(self):
        return self.command

if __name__ == "__main__":
    c = Command("\plot{f(x) = (x**2), g(x) = (x**2) h(x = (a+bc)}")
    print(c.get_math_object_information())