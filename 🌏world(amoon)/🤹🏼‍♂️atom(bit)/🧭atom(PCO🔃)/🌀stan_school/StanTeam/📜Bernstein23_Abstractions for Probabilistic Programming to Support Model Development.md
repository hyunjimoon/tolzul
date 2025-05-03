https://academiccommons.columbia.edu/doi/10.7916/d5y3-6f17

Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xv

Dedication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . xvi

Chapter 1: Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1

1.1 Probabilistic programming, brieﬂy . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1.2 Modern best practices: the Bayesian Workﬂow . . . . . . . . . . . . . . . . . . . . 5

1.3 Supporting the Bayesian Workﬂow: Program Transformations . . . . . . . . . . . 7

1.4 Contributions and roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

Chapter 2: A Systematic Review of Static Analysis of Probabilistic Programs . . . . . . . . 11

2.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

2.1.1 Introduction to Probabilistic Programming . . . . . . . . . . . . . . . . . . 11

2.1.2 Introduction to Static Analysis . . . . . . . . . . . . . . . . . . . . . . . . 13

2.1.3 Purposes of Applying Static Analysis to Probabilistic Programming . . . . 15

2.2 Technical background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2.2.1 Posterior inference . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2.2.2 Static analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

2.2.3 Probabilistic Programming from a Static Analysis and Programming Languages Perspective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

i 2.3 Properties of PPLs salient for static analysis . . . . . . . . . . . . . . . . . . . . . 33

2.3.1 Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

2.3.2 Properties of representative languages . . . . . . . . . . . . . . . . . . . . 36

2.4 Current techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

2.4.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

2.4.2 Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

2.4.3 Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

2.4.4 Usability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

2.5 Future directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

2.5.1 Extensions of current work . . . . . . . . . . . . . . . . . . . . . . . . . . 52

2.5.2 Unexplored directions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

2.6 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

Chapter 3: Multi-Model Probabilistic Programming . . . . . . . . . . . . . . . . . . . . . 59

3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

3.1.1 Uses of networks of models . . . . . . . . . . . . . . . . . . . . . . . . . 59

3.1.2 Representing networks of models . . . . . . . . . . . . . . . . . . . . . . 62

3.1.3 Swappable modules in Stan . . . . . . . . . . . . . . . . . . . . . . . . . . 64

3.1.4 Key ideas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

3.2 Related work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69

3.2.1 Comparison to ML-like module systems . . . . . . . . . . . . . . . . . . . 70

3.3 Background: Stan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

3.3.1 Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

ii 3.3.2 Effects and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

3.3.3 Program validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

3.4 Modular Stan syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

3.5 Modular Stan semantics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

3.5.1 Basic operations on programs . . . . . . . . . . . . . . . . . . . . . . . . 79

3.5.2 Structural constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

3.5.3 Module signatures and semantic constraints . . . . . . . . . . . . . . . . . 82

3.5.4 Program validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

3.5.5 Selections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

3.5.6 Semantics of modular programs and network operations . . . . . . . . . . 87

3.6 Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

3.6.1 Concretize . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

3.6.2 ModelGraph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

3.6.3 ModelNeighbors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

3.7 Additional features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

3.7.1 Append blocks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118

3.7.2 Module ﬁelds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120

3.8 Macros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122

3.8.1 Collection holes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123

3.8.2 Indexed holes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124

3.8.3 Hole instances and hole copies . . . . . . . . . . . . . . . . . . . . . . . . 124

3.8.4 Multi-ranges and range exponents . . . . . . . . . . . . . . . . . . . . . . 126

3.8.5 Hole products and hole exponents . . . . . . . . . . . . . . . . . . . . . . 127

iii 3.8.6 Example application of macros . . . . . . . . . . . . . . . . . . . . . . . . 128

3.9 Example applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

3.9.1 Interactive web interface . . . . . . . . . . . . . . . . . . . . . . . . . . . 132

3.9.2 “Golf” case study: Modular Stan for ease and clarity of development . . . . 134

3.9.3 “Birthday” case study: Modular Stan as a platform for automation . . . . . 137

3.9.4 Modular Stan as tool for multiverse and sensitivity analysis . . . . . . . . . 142

3.10 Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

Chapter 4: Automatic Transformations of Probabilistic Programs for Model Checking . . . 152

4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

4.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153

4.2.1 Probabilistic programs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153

4.2.2 Efﬁciently sampling from model parameters . . . . . . . . . . . . . . . . . 155

4.2.3 Translation challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

4.2.4 Our approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

4.3 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

4.3.1 Factor Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159

4.3.2 Directed Acyclic Probabilistic Graphical Models . . . . . . . . . . . . . . 160

4.3.3 A relation between Factor Graphs and DAGs . . . . . . . . . . . . . . . . 164

4.3.4 Deﬁning a transformation from Factor Graphs to DAGs . . . . . . . . . . . 165

4.3.5 Computing sound transformations between Factor Graphs and DAGs . . . . 166

4.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172

4.4.1 Stan implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172

iv 4.4.2 Stan program example . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

4.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182

Chapter 5: “Pedantic Mode”: Detecting Statistical Issues in Probabilistic Programs . . . . . 184

5.1 Pedantic Mode analyses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185

5.1.1 Random variable is missing from the joint distribution . . . . . . . . . . . 186

5.1.2 Random control ﬂow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

5.1.3 Parameters with zero or multiple priors . . . . . . . . . . . . . . . . . . . 188

5.1.4 Ill-advised use of statistical distributions . . . . . . . . . . . . . . . . . . . 192

5.1.5 Poorly scaled random variables . . . . . . . . . . . . . . . . . . . . . . . . 194

5.1.6 Parameters with multiple sampling statements . . . . . . . . . . . . . . . . 195

5.1.7 Strict or nonsensical parameter bounds . . . . . . . . . . . . . . . . . . . . 196

5.2 Limitations and discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

Chapter 6: Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199

6.1 Advanced model-space search and ensemble methods . . . . . . . . . . . . . . . . 199

6.2 Model-space navigation and visualization tools . . . . . . . . . . . . . . . . . . . 201

6.3 Engineering improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201

6.4 Going beyond Stan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202

6.5 Broader vocabulary for automated program transformations . . . . . . . . . . . . . 202

6.6 Large language models and program synthesis . . . . . . . . . . . . . . . . . . . . 203

Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204

References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206