from src.interpreter import n_interpret
from src.interpreter import euclidean_interpret
from src.interpreter import computable
import numpy as np
import os

if __name__ == "__main__":
    # interpreter testing

    print("Testing basic interpreting with one variable...")
    start_time = os.times()[0]

    f = n_interpret("x**2", "x")
    assert(f(5) == 25), "expected: {}, got: {}".format(f(5), 25)
    f= euclidean_interpret("y")
    assert(f(y=5) == 5)
    f = euclidean_interpret("np.sin(y)")
    assert(f(y = 4) == np.sin(4))
    f = euclidean_interpret("z")
    assert (f(z=-1) == -1)
    f = euclidean_interpret("np.sin(z)")
    assert (f(z=3) == np.sin(3))
    f = euclidean_interpret("np.sin(y)")
    assert(f() == 0)

    end_time = os.times()[0]
    print("Finished testing basic interpreter with one variable in {} seconds \n".format(end_time - start_time))

    print("Testing basic interpreter with several variables...")
    start_time = os.times()[0]

    f = euclidean_interpret("x*y*z + x")
    assert(f(1,1,1) == 2)
    assert(f() == 0)
    assert(f(1,2,3) == 1*2*3 + 1)

    end_time = os.times()[0]
    print("Finished testing basic interpreter with several variables in {} seconds \n".format(end_time - start_time))

    print("Testing computability...")
    start_time = os.times()[0]

    assert(computable(f))
    f = euclidean_interpret("")
    assert(not computable(f))

    f = euclidean_interpret("a")
    assert(not computable(f))

    f = euclidean_interpret("np.sin(y)*z*x**2")
    assert(computable(f))

    f = euclidean_interpret("np.sin(y)*z")
    assert(computable(f))
    end_time = os.times()[0]
    print("Finished testing computability in {} seconds \n".format(end_time - start_time))