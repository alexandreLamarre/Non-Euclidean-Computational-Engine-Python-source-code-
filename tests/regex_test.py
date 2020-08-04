import os
import regex
from src.regex_match import match_function, match_closed_parentheses




if __name__ == "__main__":
    function_tests_true = ["f(x) = (x,y^2 + s^5)", "f(x,y,z) = (x^2,y*(z+x), amazing*not)"]
    function_tests_false = ["f(x)", "asdkjhlkasjdklasdjl", "f(x) = "]

    bit_false = 0
    errors = 0
    print("Start testing for strings that should not be matched to functions... \n")
    for f in function_tests_false:
        for el in match_function(f):
            bit_false =1
        if bit_false == 1:
            print("test failed for {}".format(f))
            errors += 1
        bit_false = 0


    print("Finished testing for strings that should not be matched to functions, found {} errors \n".format(errors))

    errors = 0
    bit_true = 0
    print("Start Testing for strings that should be matched to functions...")

    for f in function_tests_true:
        for el in match_function(f):
            bit_true = 1

        if bit_true == 1:
            print("test failed for {}".format(f))
        bit_true = 0
    print("Finished Testing for strings that should be matched to functions, found {} errors".format(errors))

        # assert(match_function(f) == None)