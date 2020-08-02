import parser
import numpy as np


def computable(f):
    """ Checks whether inputs to a function generated by euclidean interpreter
    are computable and Returns true or false"""
    num = np.random.rand()
    try:
         value = f(num, num, num)
         if not isinstance(value, float) and not isinstance(value, int):
            return False
    except:
        return False

    return True



def n_interpret(formula, *args1):
    """Interprets a string representing a mathematical function, into a python function
        Uses a formula and the variables to return the constructed function
        ONLY WORKS WITH PYTHON BASE OPERATIONS"""
    formula = formula.lstrip()
    formula = formula.rstrip()
    try:
        code =parser.expr(formula).compile()
    except SyntaxError:
        return ("{} syntax not reckognized".format(formula))

    #need to figure out how to split them
    vars = []
    for var in args1:
        vars.append(var)

    def f(*args):
        # need to figure out how to split them
        local_val = []
        for val in args:
            local_val.append(val)
        local_eval = zip(vars,local_val)

        locals = {}
        for el in local_eval:
            locals[el[0]] = el[1]



        return eval(code, {}, locals)

    return f

def euclidean_interpret(formula):
    """ Interprets 3dimensional functions or less using the standard x,y,z variables
    When variables aren't specified into the generated function compute the image of zero"""
    formula = formula.lstrip()
    formula = formula.rstrip()
    try:
        code = parser.expr(formula).compile()
    except SyntaxError:
        return ("{} syntax not reckognized".format(formula))

    def f(x=0, y=0, z=0):
        x = x
        y = y
        z = z
        return eval(code)

    return f




