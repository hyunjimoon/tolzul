1. The chapter introduces how learning models typically focus on single learning episodes, using the example of a child learning the word "wombat" from one labeled example.
    
2. Two fundamental questions are addressed:
- Where does the prior distribution in Bayesian models come from?
- How do current learning episodes relate to previous ones?

3. The text explains how previous learning experiences can accelerate future learning. For example, knowing other words helps children understand that new words like "wombat" likely refer to whole objects rather than parts.
4. The chapter introduces the 
5. The text explains how hierarchical learning works through examples:
- Children learn categories better when they understand general principles about categories
- Learning causal models is easier with abstract knowledge about object categories
- Learners can make inferences about biological features based on structured representations

6. The chapter defines a hierarchical Bayesian model as a probabilistic model defined over an abstraction hierarchy, where knowledge at higher levels informs reasoning at lower levels.

---

1. Learning Inductive Bias with Hierarchical Bayesian Models (title)
    
2. To make matters simple, models of learning often focus on a single learning episode.
    
3. Consider, for example, a child who learns a new concept such as "wombat" after being shown a single labeled example.
    
4. A Bayesian model might help to explain this outcome using a prior distribution that captures the expectations that the child brings to the episode.
    
5. This is a useful start, but at least two fundamental questions remain to be addressed.
    
6. First, where does the prior distribution come from?
    
7. We have seen that prior distributions play a critical role in Bayesian models, which means that it is important to think carefully about how a learner might end up with an appropriate prior for a given task.
    
8. A second, related question asks: How is the current word-learning episode related to other word-learning episodes in the child's life?
    
9. Children learn the meanings of many words, and it is important to consider how previous learning episodes can help to accelerate future ones.
    
10. For example, learning previous words may help a child to realize that a novel word such as "wombat" is more likely to refer to an entire object than to a part or a property of an object.
    
11. Exploiting previous learning episodes is typically possible whenever learners face multiple tasks from the same family—for example, children must learn the causal structure of multiple tools and artifacts, and must discover the patterns of behavior that are appropriate in multiple social contexts.
    
12. In each case, we would like to understand how children learn to learn—in other words, how learning is accelerated by discovering and exploiting common elements across tasks.
    
13. This chapter suggests that hierarchical Bayesian models can help to explain where priors come from and how children learn to learn.
    
14. The key idea that distinguishes hierarchical models from the simpler models in previous chapters is the notion of abstraction.
    
15. As figure 8.1 suggests, systems of human knowledge are often organized into multiple layers of abstraction.
    
16. Learning often requires inferences at several of these levels.
    
17. For example, an infant learning language may recognize that speech sounds are instances of phonemes, strings of phonemes go together to make words, and grammatical rules specify which sequences of words are acceptable sentences (figure 8.1a).
    
18. Visual experience may allow the infant to recognize that the world contains objects, which are composed of object parts, and that there are higher-level regularities that predict which objects are likely to be found together (figure 8.1d).
    
19. An infant observing the actions of others may recognize that these actions are often carried out in the service of goals, and that these goals are achieved by stringing together sequences of lower-level motor commands (figure 8.1b).
    
20. This chapter will focus on the remaining three examples in figure 8.1.
    
21. We consider how children learn multiple categories (figure 8.1c), how children learn multiple causal models (figure 8.1e), and how children learn about multiple properties of a set of objects (figure 8.1f).
    
22. The hierarchy in figure 8.1c suggests that children may find it easy to learn about individual categories (e.g., balls are round) if they have acquired more abstract knowledge about categories in general (e.g., that objects belonging to any given category tend to have the same shape).
    
23. The hierarchy in figure 8.1e suggests that learners may find it easy to learn a causal model involving a specific object (e.g., a tablet of Lariam) if they have acquired more abstract knowledge about categories of objects (e.g., medications can cause headaches).
    
24. Finally, the hierarchy in figure 8.1f suggests that learners may be able to make confident inferences about novel biological features if they have acquired a structured representation (such as a tree) that indicates which animals tend to have features in common.
    
25. As we will see, a hierarchical Bayesian model is a probabilistic model defined over an abstraction hierarchy like the examples in figure 8.1.
    
26. Knowledge at the higher levels sets up prior distributions that are used when reasoning at the lower levels, and probabilistic inference over the hierarchy can explain how the abstract knowledge at the upper levels is
    

(Note: The last sentence appears to be cut off in the image)

Figure 8.1 caption:  
"Systems of knowledge are often organized into several levels of abstraction. In particular, hierarchies are useful for understanding (a) language, (b) action, (c) categorization, (d) vision, (e) causal learning, and (f) property induction."

[[Noise and uncertainty]] explains state and action for secretary problem.