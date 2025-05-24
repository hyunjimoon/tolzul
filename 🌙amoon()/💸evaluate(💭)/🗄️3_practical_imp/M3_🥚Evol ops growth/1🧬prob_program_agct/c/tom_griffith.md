## BITESIZE | How AI is Redefining Human Interactions, with Tom Griffiths

_Bonus Episode • 21st May 2025 • Learning Bayesian Statistics • Alexandre Andorra_

# Contrasting Approaches to Human Rationality

| Aspect                       | Kahneman/Tversky Perspective                  | Resource Rationality Approach                   |
| ---------------------------- | --------------------------------------------- | ----------------------------------------------- |
| **Philosophical Foundation** | Measures against idealized rational standards | Considers bounded computational resources       |
| **View of Human Cognition**  | Focuses on flaws/biases/deviations            | Views decisions as efficient adaptations        |
| **Key Concepts**             | Heuristics as errors, Cognitive biases        | Bounded optimality, Computational trade-offs    |
| **Role of Constraints**      | Seen as limitations to overcome               | Central to understanding human behavior         |
| **AI Development Goal**      | Create systems that avoid human flaws         | Build systems that complement human constraints |
| **Measurement Standard**     | Comparison to perfect rationality             | Performance relative to resource limits         |
| **Practical Applications**   | Debiasing systems, Error correction           | Cognitive augmentation tools, Decision support  |

### [00:00:00 - 00:05:02] Human Intelligence vs. Machine Intelligence

**Tom Griffiths:**  
The way I think about it is that human intelligence has been shaped by a set of constraints that human minds operate under. Those constraints are quite different from the ones faced by intelligent machines.

What's characteristic of human intelligence is that all the things we learn, we learn from the data which we're going to experience in the course of a single human lifetime. This means we're intrinsically limited in the amount of data we can learn from. In order for something to be useful, you probably need to learn it relatively early in that lifetime. Realistically, we're talking about maybe 20 years of data that you're using to form most of the inductive inferences about the world. And even much of that happens in the first five years.

We learn language pretty well in the first five years of life. We've figured out most of the causal structure of our environment, although we're still fine-tuning it after that. We got most of the stuff that makes us a human being in those first five years of life.

So thing number one is limited data. The second is that we do all of that learning and thinking with a fixed amount of compute - what you're carrying around inside your head, two to three pounds of neurons. We have to use that same amount of compute for every single problem we solve, so we need to be efficient in how we use those computational resources. We need to recognize when a problem has the same structure as one we've seen before and be smart about how much time we spend thinking about any particular thing.

Number three is we have limited bandwidth for communication. If it was possible for me to transfer my brain state to you, we could easily overcome those limits on data and computation. Instead, we have to communicate by making sounds at each other - a really low bandwidth method.

Humans have developed workarounds: language to convey complicated concepts, teaching as a means of compressing information, and social institutions like science that allow us to aggregate knowledge across generations. All of that helps us overcome those constraints, but it's still not as good as perfect high bandwidth communication.

By contrast, current AI approaches scale the amount of data and compute. AI systems are trained on many human lifetimes of data, with computational resources that are easy to increase, unlike for humans. And machines have the potential to transfer states between them directly.

### [00:05:02 - 00:10:18] Human Compatibility with AI

**Alexandre Andorra:**  
If I understand correctly, you're mainly saying that the way we're going to make these generative AI learn is going to be different from the way our brains learn. Does that mean there's something we can do to build these machines in a way that complements our learning and helps it? What potential do you see, and what drawbacks are you trying to avoid?

**Tom Griffiths:**  
I don't think there's anything intrinsic to current AI building methods that has human compatibility built in. There are two properties of current AI training that contribute to this to some extent:

First, training on language or other human-generated data means these systems view the world through the lens we provided. Language is a mechanism humans developed to overcome the limited communication bottleneck, describing the world in compressed form. When you put this into an AI system, it gets knowledge about the world that's been digested through human minds, which prevents these systems from being quite as alien as they could be.

Second, the last stage of training for many AI models is reinforcement learning from human feedback (RLHF), where humans provide direct information about their preferences. This contributes to alignment between humans and machines, though in a recent paper we argue that it results more in alignment with humans' current state of knowledge, which isn't necessarily the same as having humans' best interests in mind.

For example, if you're building a chatbot to advise on purchases, unless it's receiving reinforcement based on your satisfaction after buying the product, it will focus on information that makes you satisfied at the point of purchase. This can lead to behavior a human would consider deceptive.

### [00:10:18 - 00:13:15] Representational and Conceptual Alignment

If you want to build systems designed to interact with people, there's more we could do using what we know about people. We've done work on "representational alignment," making sure models' representations match humans'.

In early work, we showed that training vision models on data containing human errors (when humans are confused) results in better representations that are more aligned with people's. Models with more human-like representations do better at learning from small amounts of data and capturing human moral judgments.

We've also explored "conceptual alignment," understanding the world in terms of the same basic concepts. Even when models correlate in their representations, they can differ in how they make sense of the world. For example, humans distinguish between different numbers of objects. Image models lose track once you get past four or five objects - which matches part of human cognition, but we also have richer conceptual representations for larger numbers.

Our AI systems currently capture part of how humans perceive the world - the part that happens quickly in less than a second - but miss the more symbolic abstract representations people form. In our paper "Machines That Learn and Think with People," we argue that to make machines engage with humans in all ways humans engage with humans, we need to capture more of what allows humans to engage with each other.

### [00:13:15 - 00:17:18] Making AI That Elevates Human Cognition

**Alexandre Andorra:**  
How can we apply what we know about human cognition to make generative AI elevate us and help us avoid biases? Rather than making AI to our perfect image, how can we make them help us become better humans?

**Tom Griffiths:**  
My first response would be that it's not clear our objective should be building AI systems that are like people. Human minds are a consequence of an evolutionary process reflecting various biological constraints. It might be better to think about what's the best way to build intelligent systems that aren't like people in terms of what's easy to engineer, but are easy for people to interact with.

If you think about birds and jet planes - studying how birds fly was incredibly important for making the first airplane, understanding aerodynamics and lift. But once you have something flying, you can engage in an iterative process leading to jet planes, which are very different from birds. That's a reasonable place to end up.

There are reasons to incorporate some bird-like properties into planes, like efficiency in fuel consumption. Birds are amazing flying machines, but if your goal is getting from one location to another as fast as possible, learning more about jet engines is the way to go.

Similarly with AI - there's plenty we can still learn from human cognition, but our objective shouldn't necessarily be to build something human-like.

### [00:17:18 - 00:22:05] Resource Rationality and AI-Assisted Decision Making

That said, there are plenty of ways AI can help humans. I work on understanding human decision making, following experiments by Kahneman and Tversky showing that people are bad at making decisions according to expected utility theory.

Expected utility theory tells us what we should be doing, but it couldn't be achieved by any real entity in the world. It says for each possible outcome, evaluate the utility, evaluate the probability, take the expectation. In real life, this is impossible - you'd spend your entire life thinking about possible outcomes.

Most decisions must be made under time constraints, which are intrinsic to the problem and a consequence of the algorithms we can execute on our human brains.

In the 1980s, computer scientists like Stuart Russell and Eric Horvitz developed "bounded optimality" - the idea that a bounded optimal agent uses the best possible algorithm for making a decision, considering not just the outcomes but also the computational cost of executing that algorithm.

We've expanded this in an approach called "resource rationality" - the idea that being rational means making rational use of limited cognitive resources to do the best you can. When we re-evaluate human decisions through this lens, many decisions that deviate from expected utility theory actually make sense from a resource rationality perspective.

This gives us a perspective on how to help humans make better decisions - by increasing the computational resources available to them. Instead of putting chips in people's brains like Elon Musk is trying to do, we can use AI systems to put more compute in human environments.

We can partially pre-solve problems and give you information in a more accessible way, putting relevant information in easily accessible places or providing information about payoffs that supplements what's immediately available.

One of my collaborators, Falk Lieder, has worked on gamified to-do lists where you specify what you want to do and how valuable each task is. It automatically calculates how many points you get for completing tasks, giving immediate rewards as the points add up. Experiments have shown this can help reduce procrastination.

These are ways of using AI to help humans without having to build something that's human-like.