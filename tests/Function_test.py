from src.Function import Function
from src.regex_match import match_function


if __name__ == "__main__":
    s = ''
    print("hello")
    while(s != "q"):

        temp = match_function(s)

        bit_false = 1
        funcs = []
        for f in temp:
            bit_false = 0
            funcs.append(f.group(0))
        print("Interpreted {} as {}".format(s,funcs))

        for f in funcs:
            test = Function(f)
            print("Input to Function Object Declaration : {}".format(f))
            print("Result : '{}'".format(test))


        if(bit_false == 1):
            print("input {} could not be parsed as a function".format(s))

        s = input()