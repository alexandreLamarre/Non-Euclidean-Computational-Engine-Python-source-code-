import parser
from math import *
from src.Error_Stack import ErrorStack
import numpy as np

class Function(ErrorStack):
    def __init__(self, function_string):
        """
        (String) -> None
        Takes in a Function String preprocessed by match()
        """
        super().__init__()
        self.name, self.str_vars, self.str_funcs = self._parse_input(function_string)
        self.funcs = self.create_funcs(self.str_funcs)
        self.in_dimension = len(self.str_vars)
        self.out_dimension = len(self.str_funcs)

        #test evaluation to check compiler errors
        test_input = [0] * self.in_dimension
        self.evaluate(*test_input)

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
        for i in range(len(function_set)):
            function_set[i] = function_set[i].strip()

        name_var = name_var.strip()
        name_var = name_var.split('(')

        name = name_var[0]
        name = name.strip()

        var = name_var[1]
        var = var.strip()
        var = var[:-1]
        var = var.split(",")
        for i in range(len(var)):
            var[i] = var[i].strip()
        return name, var, function_set

    def create_compiled_code(self, str_funcs):
        """
        (String[], String[]) -> (function[])
        """
        # use a variation of n-interpreter.
        code_list = []
        for f in str_funcs:
            try:
                f2 = f.replace("^", "**")
                code = parser.expr(f2).compile()
                code_list.append(code)
            except SyntaxError:
                # self.push_errors("Invalid function {}".format(f))
                self.push_error("'{}' :Could not interpret this function in the compiler. Stopping execution...\n".format(f))
                self.set_stop()
        return code_list

    def create_eval_functions(self, code_list):
        """
        (Compiled code[]) -> (functions [])
        """
        function_list = []
        for j in range(len(code_list)):
            def make_func(j):
                def f(vars, *args):
                    """
                    (Vars)x (value1, value2, ...) -> (float)
                    """
                    assert(len(vars) == len(args))
                    for i in range(len(vars)):
                        exec_str = "{}={}".format(vars[i], args[i])
                        exec(exec_str)
                    return eval(code_list[j])
                return f

            function_list.append(make_func(j))

        return function_list

    def create_funcs(self, str_funcs):
        """
        (String[]) -> (functions [])
        """
        code_list = self.create_compiled_code(str_funcs)
        return self.create_eval_functions(code_list)

    def evaluate(self, *args):

        res = []
        for i in range(len(self.funcs)):
            try:
                value = self.funcs[i](self.str_vars, *args)
                res.append(value)
            except:
                self.push_error("'{}' could not be evaluated as a numeric function in user defined function '{}' \n".format(self.str_funcs[i], self.name))
                self.set_stop()
                res.append(None)

        return res

    def get_codomain_functions(self):
        return self.funcs

    def get_vars(self):
        return self.str_vars
    def is_recursive(self):
        if self.name in self.str_vars:
            return False
        elif (self.name) in self.str_funcs:
            # consider the case where
            return True

    def __repr__(self):
        output_str = ""
        var_to_str = ""
        for v in self.str_vars:
            var_to_str += v + ','
        var_to_str = var_to_str[:-1]

        func_to_str = ""
        for f in self.str_funcs:
            func_to_str += f + ','
        func_to_str = func_to_str[:-1]
        output_str = "NAME: {} VARS: [{}] FUNCS [{}]".format(self.name, var_to_str, func_to_str)

        return output_str

if __name__ == "__main__":
    pass
    # input_test = input()
    # while(input_test):
    #     test = match_function(input_test)
    #     for t in test:
    #         func = Function(t)
    #         print(func)
    #         print('\n')
    #     input_test = input()

    #test = match_function("laplace(x,y,z) = (x** (1/3), y**(1/3), z**(1/3)) fourrier(x) = (sin(x^5))")
    #     for t in test:
    #         func = Function(t)
    #         print(func)
    #         print('\n')

