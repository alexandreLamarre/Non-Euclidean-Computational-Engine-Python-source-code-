from interpreter import FunctionInterpreter
from Error_Stack import ErrorStack
from Function import Function

class FunctionManager(FunctionInterpreter):
    def __init__(self, function_strs):
        """
        (String[]) -> (None)
         Initializes a Function Manager with a set of Functions
        """
        super().__init__()
        self.Functions_str_container = self.match(function_strs)
        self.uninterpreted = self.process_uninterpreted(function_strs)

        self.Functions_container = [Function(f) for f in self.Functions_str_container]

    def process_uninterpreted(self, in_str):
        res = in_str
        for fstr in self.Functions_str_container:
            assert(fstr in res), "Interpreted input was not even in the input to begin with??"
            start_index = res.find(fstr)
            end_index = start_index+len(fstr)
            res = res[0:start_index].strip() +"\n"+ res[end_index:].strip()
            res.strip()
        return res

    def get_uninterpreted(self):
        output = self.uninterpreted.strip()

        return "The following could not be interpreted as a function : \n" + output if output else ""

    def get_interpreted(self):
        res = ''
        for f in self.Functions_str_container:
            res += f
            res += '\n'
        res = res.strip()
        return "Interpreted input functions:" + "\n" +res if res else ""

    def get_compile_errors(self):
        errors = ""
        for f in self.Functions_container:
            input_values = [0]*f.in_dimension
            f.evaluate(*input_values)
            errors += f.check_errors()
        return errors

    def generate_uninterpreted_reason(self):
        pass

if __name__ == "__main__":
    test = FunctionManager("laplace(x,y,z) = (x, y**(1/3), z**(1/3)) fourrier(x) = (x//y)}")
    print(test.get_compile_errors())