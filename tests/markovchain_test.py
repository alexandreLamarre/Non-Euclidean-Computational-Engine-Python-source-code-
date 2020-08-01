from src.markovchain import Chain

if __name__ == "__main__":
    states = ["a", "b" , "c"]
    transitions = [[0,1/2,1/2], [1/3,1/3,1/3], [0,1,0]]
    c = Chain(states, transitions)

    print("Testing Initialization of Chain...")
    assert(c.get_states() == ["a", "b", "c"])

    assert(c.get_transitions() == {'a': [0, 0.5, 0.5], 'b': [0.3333333333333333,\
                        0.3333333333333333, 0.3333333333333333], 'c': [0, 1, 0]})

    print("Testing of Initialization of Chain successful")


    print("\nTesting Markov Chain properties of Chain...")
    for i in range(10000):
        res = c.pick_random(c.get_transitions()["a"])
        assert(res != None)
        assert(res < len(c.get_states()))

    for i in range(10000):
        res = c.step("a")
        assert(res == "b" or res == "c")

        res = c.step("b")
        assert(res == "a" or res == "b" or res == "c")

        res = c.step("c")
        assert(res == "b")

    for i in range(100):
        res= c.n_orbit("a")

    print("Testing Markov Chain properties of Chain Successful")