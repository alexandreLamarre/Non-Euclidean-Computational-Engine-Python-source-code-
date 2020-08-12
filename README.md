# NE Computational Engine

## Foreword

A computational engine is hard to define, but easy to recognize. 
In general a computation engine takes some aggregation of data and returns a meaningful result. This implementation of a computationalal engine 
takes symbolic mathematical input from the user, computes its properties and returns them in a way humans can understand. 
 
Traditionally, other mathematical computational engines like Wolfram Alpha(now computational intelligence) focus on 
the fixed three dimensions that we've all seen in high school geometry, high school algebra and college calculus. 
These methods represent simple ways to interpret phenomena and are Euclidean in nature.
In this computational engine, we aim to take things further by also interpreting
the properties of mathematical objects that produce things that are non-euclidean in nature. 
  

## Table of Contents
- [The goal](#The-goal)
- [Features](#Features)
- [Quick guide](#Quick-guide)
- [Code architecture](#Code-architecture)
- [Implementation details](#Implementation-details)
- [Known issues](#Known-issues)
- [External Libraries](#External-Libraries)
- [References](#References)

## The goal:

- 

## Features: 
- Command interpreter for commands of the form`\command_name{arguments}`
- Function Interpreter:
  - Interprets **custom** mathemtical functions from input into python computable functions
  - Makes use of the math standard library for python
  
- Plotting functions from custom mathematical functions for:
  - Functions from R to R <sup></sup> using a traditional graph
  - Functions from R to R<sup>2</sup> using meshgrid technology
  - Functions from R<sup>2</sup> to R using meshgrid technology
  - Functions from R<sup>2</sup> to R<sup>2</sup> using contour maps
  
  
 
## Quick guide:

- 


## Implementation details

- Function variables overshadow math standard 
library variables and functions. 
    - For example,
`f(e) = (e^2)` is equivalent to `g(x) = (x^2)` and to use the 
math constant e in `f` we would have to refer to it as
`f(e) = (math.e * e^2)` which is equivalent to `g(x) = (e* x^2)`


<!---
- Iterated Function Systems:
  - [x] Plot 
  - [ ] Associated Markov Chain
  - [ ] Dimension computations
 
- Markov Chains
  - [ ] Visualizer 
  - [ ] Encoding
  - [ ] Properties Evaluator
 
 - Group Theory
   - [ ] Group operations
 
 - Galois Theory
   - [ ] Exact roots of polynomials
   - [ ] Properties Evaluator
--->

## Known issues
- Complex casting happens in exponential and logarithmic functions 
in contour maps from R<sup>2</sup> to R<sup>2</sup> when they involve multiple
variables when complex casting should not occur. Issue likely has to do with the 
implementation of the math standard library. 
- New labels overlap on labels of previously computed plots. 
Supposed to be resolved in a future version of matplotlib.  

## External Libraries
- [NumPy](https://numpy.org/doc/)
- [Matplotlib](https://matplotlib.org/)
- [regex](https://pypi.org/project/regex/)
- [SymPy](https://www.sympy.org/en/index.html)

## References
  

  - Tucker, Alan. "Applied Combinatorics" 6th edition 2012
  - Munkres, James R. "Topology" 2nd edition. 2018.
  - Fisher, Stephen D. "Complex Variables" 1990.
  - Folland, Gerald B.  "Advanced Calculus" 2002.
