## compiler vs transpiler

compiler: some programming language -> assembly instructions of the target machine architecture
transpiler: some programming language -> another programming language

## Representing programs as data structures
We write expressions in programming languages as a string. For example, `1 + 1 * 2` indicates two operations on 3 integers. 

Instead of directly working with strings we utilize data structures, which gives us a way to easily manipulate and process "structures". String manipulation is clunky. So how can we represent that we're doing a multiplication and an addition operation here? A straightforward way is through compositions of functions, like so:

`add(integer(1), mul(integer(1), integer(2)))`

This adds "structure", allowing the computer to, for example, access operands and results easier than the string variant.

So how do we convert a string into a data structure? We first perform [lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis) (using a scanner in compiler design), which tokenizes the input string into lexical tokens. You can think of this is identifying and separating words in a sentence into nouns, verbs, and so on. In programming languages, you can separate them into say, identifiers, operators, constants.

Once a scanner performed lexical analysis, we check that the program is in the grammar form the compiler expects, and if so identify the program structure according to the grammar. This is called [parsing](https://en.wikipedia.org/wiki/Parsing) and is a well-researched topic. Rat uses an algorithm called [Pratt parsing](https://en.wikipedia.org/wiki/Operator-precedence_parser#Pratt%20parsing), which is a operator-precedence parser that works on literals. The parser outputs something called an AST(abstract syntax tree), which is a tree structure of the program.

The AST is a rudimentary computation graph - it is possible to perform computations through it. However, it's often inconvenient to directly do so because the AST is only created from syntactic rules. The process of compilation "lowers" the level of a language, meaning that we need more details of how the program works to generate code. In standard compilers, compilers augument the AST with context-specific information to generate an IR(intermediate representation). IR is another data structure, that holds additional information such as variable scopes and control flow. It also lowers the AST into a set of generic functions, allowing easier analysis and optimization without and syntax invonved. Common compilers, such as G++ and the LLVM suite perform optimization on the IR. Rat does not emit an IR; it was deemed unnecessary due to it being a simpler language and less optimizations being available.

Once the optimizations on the IR is complete, the compiler transforms the data structure into the target language, such as assembly or some other programming language. For g++, it means it emits assembly code. For stanc3, it emits a C++ program. For Rat, it emits a Python module. The resulting ouput can be fed to its respective "machine"(processor for assembly, a C++ compiler for stanc3, Python interpreter for Rat), which runs the program.
## Necessities of a probabilistic program

Consider we're trying to represent some probabilistic model in the form of a program. What would be required so that faithful computation is possible? A probabilistic program denotes a target joint density. That means a function is needed for calculating the log density, for ease of calculation and numerical stability. If we're using gradient based inference methods its derivative, along with a system for dealing with variable constraints and change of variables are required. We can think of the basic steps of performing inference as the following:

1. *Draw* a sample according to the program's log density
2. *Constrain* the parameters according to the program's specifications
3. *Transform* parameters if required according to the program's specifications.

Thus a compiled probabilistic program needs to provide functions for each step. The goal of compilation in rat is to provide these primitive functions so that inference can be correctly done.

## JIT
What's JIT? Normally we compile our programs after we're finished writing the code, and before running it. This is done just once, until we change the code. Just in Time compilation performs compilation every time before you run your program. This gives a couple of advantages:

1. The JIT compiler can better take advantage of the machine's specialized instructions/architecture.
2. Code optimizations can be done adaptively 
But since there's a compilation step before you run the program, there is a significant overhead. The tradeoff should be weighted to make sure JIT is worth(For simpler programs it might not be worth it).


input: a
a * b

if a == 2:
b << 2

https://github.com/Dashadower/advi/blob/master/models.py

abstract syntax tree - context of parsing syntactic separation
computation graph - context of operations and functions
factor graph - + control flow and model-specific contexts

expression vs statement