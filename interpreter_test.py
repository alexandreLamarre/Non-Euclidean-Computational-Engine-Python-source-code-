from interpreter import n_interpret
from interpreter import euclidean_interpret
from interpreter import computable
import numpy as np
import os

if __name__ == "__main__":
    # interpreter testing
    #interpreter testing


    f = euclidean_interpret("np.sin(x)")
    print(f(5))

    print("Testing interpreting with one variable...")

    start_time = os.times()[0]

    f = n_interpret("x**2", "x")
    assert(f(5) == 25), "expected: {}, got: {}".format(f(5), 25)

    # f = interpret("np.sin(x)", "x")
    # assert(f(1) == np.sin(1))

    end_time = os.times()[0]
    print("Finished testing interprter with one variable in {}".format(end_time - start_time))