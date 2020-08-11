# NE Computational Engine

## Foreword

A computational engine is hard to define, but easy to reckognize. 
In general a computation engine takes some aggregation of data and returns a meaningful result. This implementation of a computational engine 
takes symbolic mathematical input from the user, computes its properties and returns them in a way humans can understand. 
 
Traditionally, other mathematical computational engines like Wolfram Alpha(now computational intelligence) focus on 
the fixed three dimensions that we've all seen in highschool geometry, highschool algebra and college calculus. 
These methods represent simple ways to interpret phenomena and are euclidean in nature.
In this computational engine, we aim to take things further and also interpret
the properties of mathematical symbols that produce things that are non-euclidean in nature. 
  

## Table of Contents
- [The goal](#The goal)
- [Features](#Features)
- [Quick guide](#Quick guide)
- [Implementation details](#Implementation details)
- [External Libraries](#variable-name-conventions)
- [References](#References)

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
