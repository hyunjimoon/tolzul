DreamCoder: growing generalizable, interpretable knowledge with wake–sleep Bayesian program learning

Kevin Ellis 1 , Lionel Wong 2 , Maxwell Nye 2 ,

keyword: program synthesis, expertise, Bayesian program learning

Expert problem-solving is driven by powerful languages for thinking about problems and their solutions. Acquiring expertise means learning these languages—systems of concepts, alongside the skills to use them. We present DreamCoder, a system that learns to solve problems by writing programs. It builds expertise by creating domain-speciﬁc programming languages for expressing domain concepts, together with neural networks to guide the search for programs within these languages. A ‘wake–sleep’ learning algorithm alternately extends the language with new symbolic abstractions and trains the neural network on imagined and replayed problems. DreamCoder solves both classic inductive programming tasks and creative tasks such as drawing pictures and building scenes. It rediscovers the basics of modern functional programming, vector algebra and classical physics, including Newton’s and Coulomb’s laws. Concepts are built compositionally from those learned earlier, yielding multilayered symbolic representations that are interpretable and transferrable to new tasks, while still growing scalably and ﬂexibly with experience.

This article is part of a discussion meeting issue ‘Cognitive artiﬁcial intelligence’.