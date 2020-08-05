class Function:
    def __init__(self, function_string):
        """
        (String) -> None
        Takes in a Function String
        """
        self.name, self.str_vars, self.str_funcs = self._parse_input(function_string)
        self.funcs = None

    def _parse_input(self, function_matched_string):
        """
        (String) -> (String, String[], String[])

        Takes a string from match_function() to return attributes to be used by
        Function class
        """

        namevar_split_functions = function_matched_string.split("=")
        name_var = namevar_split_functions[0]

        function_set = namevar_split_functions[1]
        function_set = function_set.strip()
        function_set = function_set[1:-1]
        function_set = function_set.split(',')

        name_var = name_var.strip()
        name_var = name_var.split('(')

        name = name_var[0]
        name = name.strip()

        var = name_var[1]
        var = var.strip()
        var = var[:-1]
        var = var.split(",")

        return name, var, function_set

    def create_compile_funcs(self, str_vars,str_funcs):
        """
        (String[], String[]) -> (function[])
        """
        # use a variation of n-interpreter.
        pass

    def __repr__(self):
        output_str = ""
        var_to_str = ""
        for v in self.str_vars:
            var_to_str += v + ' , '

        func_to_str = ""
        for f in self.str_funcs:
            func_to_str += f + ' , '
        output_str = "name: {}, variables: {} functions {}".format(self.name, var_to_str, func_to_str)

        return output_str