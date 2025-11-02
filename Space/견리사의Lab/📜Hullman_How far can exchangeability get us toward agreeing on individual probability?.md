---
collection:
  - "[[Papers]]"
author_ids:
  - hullman
field:
  - 🐢inv
created: 2025-01-26
---

This is Jessica. What’s the common assumption behind the following? 

- Partial pooling of information over groups in hierarchical Bayesian models 
-  In causal inference of treatment effects, saying that the outcome you would get if you were treated (Y^a) shouldn’t change depending on whether you are assigned the treatment (A) or not
- Acting as if we believe a probability is the “objective chance” of an event even if we prefer to see probability as an assignment of betting odds or degrees of belief to an event

The question is rhetorical, because the answer is in the post title. These are all examples where statistical exchangeability is important. Exchangeability says the joint distribution of a set of random variables is unaffected by the order in which they are observed. 

Exchangeability has broad implications. Lately I’ve been thinking about it as it comes up at the ML/stats intersection, where it’s critical to various methods: achieving coverage in [conformal prediction](https://arxiv.org/abs/2107.07511), using counterfactuals in [analyzing algorithmic fairness](https://dl.acm.org/doi/pdf/10.1145/3351095.3372851), [identifying independent causal mechanisms](https://arxiv.org/pdf/2405.18836) in observational data, etc. 

This week it came up in the course I’m teaching on [prediction for decision-making](https://statmodeling.stat.columbia.edu/2024/12/06/new-course-prediction-for-individualized-decision-making/). A student asked whether exchangeability was of interest because often people aren’t comfortable assuming data is IID. I could see how this might seem like the case given how application-oriented papers (like on conformal prediction) sometimes talk about the exchangeabilty requirement as an advantage over the usual assumption of IID data. But this misses the deeper significance, which is that it provides a kind of practical consensus between different statistical philosophies. This consensus, and the ways in which it’s ultimately limited, is the topic of this post.

**Interpreting the probability of an individual event**

One of the papers I’d assigned was Dawid’s “On Individual Risk,” which, as you might expect, talks about what it means to assign probability to a single event. Dawid distinguishes “groupist” interpretations of probability that depend on identifying some set of events, like the frequentist definition of probability as the limiting frequency over hypothetical replications of the event, from individualist interpretations, like a “personal probability” reflecting the beliefs of some expert about some specific event conditioned on some prior experience. For the purposes of this discussion, we can put Bayesians (subjective, objective, and pragmatic, as Bob describes them [here](https://statmodeling.stat.columbia.edu/2024/07/10/three-cultures-bayes-subjective-objective-pragmatic/)) in the latter personalist-individualist category. 

On the surface, the frequentist treatment of probability as an “objective” quantity appears incompatible with the individualist notion of probability as a descriptor of a particular event from the perspective of the particular observer (or expert) ascribing beliefs. If you have a frequentist and a personalist thinking about the next toss of a coin, for example, you would expect the probability the personalist assigns to depend on their joint distribution over possible sequences of outcomes, while the frequentist would be content to know the limiting probability. But de Finetti’s theorem shows that if one believes a sequence of events to be exchangeable, then you can’t distinguish their beliefs about those random variables from conceiving of independent events with some underlying probability. Given a sequence of exchangeable Bernoulli random variables X1, X2, X3, … , you can think of a draw from their joint distribution as sampling _p ~ mu_, then drawing X1, X2, X3, … from _Bernoulli(p)_ (where mu is a distribution on [0,1]). So the frequentist and personalist can both agree, under exchangeability, that _p_ is meaningful for decision making. David Spiegalhalter recently published an [essay on interpreting probability](https://www.nature.com/articles/d41586-024-04096-5) that he ended by commenting on how remarkable this pragmatic consensus is.

But Dawid’s goal is to point out ways in which the apparent alignment is not as satisfactory as it may seem in resolving the philosophical chasm. It’s more like we’ve thrown a (somewhat flimsy) plank over it. Exchangeability may sometimes get us across by allowing the frequentist and personalist to coordinate in terms of actions, but we have to be careful how much weight we put on this.  

**The reference set depends on the state of information**

One complication is that the personalist’s willingness to assume exchangeability depends on the information they have. Dawid uses the example of trying to predict the exam score of some particular student. If they have no additional information to distinguish the target student from the rest, the personalist might be content to be given an overall limiting relative frequency _p_ of failure across a set of students. But as soon as they learn something that makes the individual student unique, _p_ is no longer the appropriate reference for the individual student’s probability of passing the exam. 

As an aside, this doesn’t mean that exchangeability is only useful if we think of members of some exchangeable set as identical. There may still be practical benefits of learning from the other students in the context of a statistical model, for example. See, e.g., Andrew’s previous post on exchangeability as an [assumption in hierarchical models](https://statmodeling.stat.columbia.edu/2022/11/24/understanding-exchangeability-in-statistical-modeling-a-thanksgiving-themed-post/), where he points out that assuming exchangeability doesn’t necessarily mean that you believe everything is indistinguishable, and if you have additional information distinguishing groups, you can incorporate that in your model as group-level predictors.

But for the purposes of personalists and frequentists agreeing on a reference for the probability of a specific event, the dependence on information is not ideal. Can we avoid this by making the reference set more specific? What if we’re trying to predict a particular student’s score on a particular exam in a world where that particular student is allowed to attempt the same exam as many times as they’d like? Now that the reference group refers to the particular student and particular exam, would the personalist be content to accept the limiting frequency as the probability of passing the next attempt? 

The answer is, not necessarily. This imaginary world still can’t get us to the generality we’d need for exchangeability to truly reconcile a personalist and frequentist assessment of the probability. 

**Example where the limiting frequency is constructed over time**

Dawid illustrates this by introducing a complicating (but not at all unrealistic) assumption: that the student’s performance on their next try on the exam will be affected by their performance on the previous tries. Now we have a situation where the limiting frequency of passing on repeated attempts is constructed over time. 

As an analogy, consider drawing balls from an urn, where when we draw our first ball, there is 1 red ball and 1 green ball in it. Upon drawing a ball, we immediately return and add an additional ball of the same color. At each draw, each ball in the urn is equally likely of being drawn, and  the sequence of colors is exchangeable. 

Given that _p_ is not known, which do you think the personalist would prefer to consider as the probability of a red ball on the first draw: the proportion of red balls currently in the urn, or the limiting frequency of drawing a red ball over the entire sequence? 

Turns out in this example, the distinction doesn’t actually matter: the personalist should just bet 0.5. So why is there still a problem in reconciling the personalist assessment with the limiting frequency?

The answer is that we now have a situation where knowledge of the dynamic aspect of the process makes it seem contradictory for the personalist to trust the limiting frequency. If they know it’s constructed over time, then on what ground is the personalist supposed to assume the limiting frequency is the right reference for the probability on the first draw? This gets at the awkwardness of using behavior in the limit to think about individual predictions we might make.

**Why this matters in the context of algorithmic decision-making**

This example is related to some of my prior posts on why calibration does not satisfy everyone as a means of ensuring good decisions. The broader point in the context of the course I’m teaching is that when we’re making risk predictions (and subsequent decisions) about people, such as in deciding who to grant a loan or whether to provide some medical treatment, there is inherent ambiguity in the target quantity. Often there are expectations that the decision-maker will do their best to consider the information about that particular person and make the best decision they can. What becomes important is not so much that we can guarantee our predictions behave well as a group (e.g., calibration) but that we understand how we’re limited by the information we have and what assumptions we’re making about the reference group in an individual case. 

This entry was posted in [Bayesian Statistics](https://statmodeling.stat.columbia.edu/category/bayesian-statistics/), [Causal Inference](https://statmodeling.stat.columbia.edu/category/causal-inference/), [Decision Analysis](https://statmodeling.stat.columbia.edu/category/decision-theory/), [Miscellaneous Science](https://statmodeling.stat.columbia.edu/category/miscellaneous-science/), [Miscellaneous Statistics](https://statmodeling.stat.columbia.edu/category/miscellaneous-statistics/) by [Jessica Hullman](https://statmodeling.stat.columbia.edu/author/jessica/). Bookmark the [permalink](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/ "Permalink to How far can exchangeability get us toward agreeing on individual probability?").

## 13 thoughts on “How far can exchangeability get us toward agreeing on individual probability?”

1. ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=68&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [January 17, 2025 5:02 PM at 5:02 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387887) said:
    
    Jessica:
    
    Thanks for linking to my Thanksgiving-themed post!
    
    I’ve found statisticians and computer scientists to often be very confused about exchangeability, which is annoying because it’s pretty simple from my perspective. There’s this weird mysticism around “exchangeability” or “transportability,” which seems really misguided to me, given that literally all of statistics is about generalization, that is, about using data from one place and using this to make inference about some other place.
    
    Here are some relevant blog discussions from a few years back: [Long discussion about causal inference and the use of hierarchical models to bridge between different inferential settings](https://statmodeling.stat.columbia.edu/2012/07/16/long-discussion-about-causal-inference-and-the-use-of-hierarchical-models-to-bridge-between-different-inferential-settings/) with a [followup here](https://statmodeling.stat.columbia.edu/2012/07/23/examples-of-the-use-of-hierarchical-modeling-to-generalize-to-new-settings/).
    
    People see extrapolation as an all-or-nothing thing, which leads to three errors: (1) thinking that in classical designs such as sample surveys and randomized experiments that there’s no extrapolation challenge at all, (2) naively thinking that if you don’t have a perfect random sample or randomized experiment that you can’t do anything, and (3) in problems where generalization is required, not thinking about it clearly as a statistical problem.
    
    This general issue arises in many engineering problems, where people bounce back and forth between blindly following a model (and its “guarantees”), or nihilististically saying that nothing can be done because the model is false.
    
    Anyway, if there’s a way I could adapt these thoughts to the specific problem at hand, I’d be happy to have the opportunity to do so.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387887#respond)
    
    - ![](https://secure.gravatar.com/avatar/5a5f42297e33f2776eb42b2059a4870f?s=39&d=identicon&r=g)[Jessica Hullman](http://users.eecs.northwestern.edu/~jhullman/) on [January 17, 2025 9:03 PM at 9:03 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387902) said:
        
        I’m still thinking about the connective tissue in that Thanksgiving stew :-)
        
        >People see extrapolation as an all-or-nothing thing, which leads to three errors: (1) thinking that in classical designs such as sample surveys and randomized experiments that there’s no extrapolation challenge at all, (2) naively thinking that if you don’t have a perfect random sample or randomized experiment that you can’t do anything, and (3) in problems where generalization is required, not thinking about it clearly as a statistical problem.
        
        >This general issue arises in many engineering problems, where people bounce back and forth between blindly following a model (and its “guarantees”), or nihilististically saying that nothing can be done because the model is false.
        
        These statements ring so true from where I sit in computer science!
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387902#respond)
        
2. ![](https://secure.gravatar.com/avatar/?s=68&d=identicon&r=g)Anonymous on [January 17, 2025 7:00 PM at 7:00 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387896) said:
    
    On the subject of exchangeability, I’ve always liked this paper:
    
    [https://bayes.wustl.edu/etj/articles/applications.pdf](https://bayes.wustl.edu/etj/articles/applications.pdf)
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387896#respond)
    
    - ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [January 17, 2025 7:09 PM at 7:09 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387899) said:
        
        Anon:
        
        We discuss some of these issues in chapter 5 of Bayesian Data Analysis; see exercises 4, 5, and 6 at the end of that chapter.
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387899#respond)
        
        - ![](https://secure.gravatar.com/avatar/cbf7434d6ca709804bad6c7935a64048?s=39&d=identicon&r=g)Carlos Ungil on [January 20, 2025 3:31 PM at 3:31 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388065) said:
            
            The distribution in exercise 4 cannot be written as a mixture – unless you allow for negative weights.
            
            The covariances for the mixture of in exercise 5 are nonnegative – unless you allow for negative weights.
            
            Even though this has nothing to do with the quantum realm one may also want to have negative weights in this mathematical decomposition. However, it would be confusing to call the resulting entity a “probabilistic mixture”.
            
            [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2388065#respond)
            
            - ![](https://secure.gravatar.com/avatar/d582b760aff3a7d7ce1197505fb57837?s=39&d=identicon&r=g)[Andrew](http://www.stat.columbia.edu/~gelman/) on [January 20, 2025 3:37 PM at 3:37 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388066) said:
                
                Carlos:
                
                That’s the whole point of exercise 4, that it’s not a mixture! Indeed, exercise 4(b) is “Show that this distribution cannot be written as a mixture of independent and identically distributed components.”
                
                In exercise 5, there are no “weights”; there are only probabilities. In BDA, we follow the standard rules of probability, in which probabilities are real numbers between 0 and 1.
                
            - ![](https://secure.gravatar.com/avatar/cbf7434d6ca709804bad6c7935a64048?s=39&d=identicon&r=g).Carlos Ungil on [January 20, 2025 3:50 PM at 3:50 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388067) said:
                
                One can also write books on Quantum Mechanics following the standard rules of probability, in which probabilities are real numbers between 0 and 1.
                
                It was just an example – that may not be known to every reader – of how “generalized probabilities” may be mathematically convenient in “classical” problems to work around those limitations. (The inconvenient part is of course that they are no longer probabilities!)
                
    - ![](https://secure.gravatar.com/avatar/5a5f42297e33f2776eb42b2059a4870f?s=39&d=identicon&r=g)[Jessica Hullman](http://users.eecs.northwestern.edu/~jhullman/) on [January 17, 2025 9:04 PM at 9:04 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387903) said:
        
        Thanks, I was meaning to go back to Jaynes after this post!
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387903#respond)
        
    - ![](https://secure.gravatar.com/avatar/cbf7434d6ca709804bad6c7935a64048?s=39&d=identicon&r=g)Carlos Ungil on [January 20, 2025 3:11 PM at 3:11 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388064) said:
        
        Thanks for the link.
        
        Looking for papers citing that one I found “A review of extended probabilities” which is quite interesting in the context of the recent “the rules of probability fail in the quantum realm” discussion.
        
        [https://bayes.wustl.edu/etj/articles/review.extended.prob.pdf](https://bayes.wustl.edu/etj/articles/review.extended.prob.pdf)
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2388064#respond)
        
3. ![](https://secure.gravatar.com/avatar/?s=68&d=identicon&r=g)Anonymous on [January 19, 2025 9:47 AM at 9:47 am](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387968) said:
    
    “This example is related to some of my prior posts on why calibration does not satisfy everyone as a means of ensuring good decisions. ”
    
    But of course that’s not the objective of calibration or of “decision making” regarding loans or medical treatment.
    
    Regarding loans, the objective is to generate a *profitable* loan, rather than a process that would “satisfy everyone”. In fact, if loans are not profitable, they are not made at all. Many societies throughout history have imposed or held prohibitions against lending for profit – always to their detriment. The amount of money available to borrow shrinks rapidly under these conditions and everyone suffers – including the people who think they are being mistreated by the “decision making” about loans.
    
    If we enforce profitability for lending, then any siginficant “malism” in the “decision making” about lending would imply a significant business opportunity, right? Companies are leaving money on the table. Our poltiical and economic system provides a simple way to force companies to address such a theoretical malism: develop a competitive firm that corrects the “malism” and takes away their business.
    
    So the theoretical question is interesting in its own right but with regard to specific applications, the question is empirical: do the loans generate profit or not? The theoretical expressions that underly the “decision making” must conform to reality – and to reality measured by the actual quantitative objective, not one measured by the vague concept of “satisfy everyone”.
    
    Medical decision making is more complex because the objective is less clear and varies according to different situations, but ultimately society can’t expend more resources than it creates.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387968#respond)
    
    - ![](https://secure.gravatar.com/avatar/5a5f42297e33f2776eb42b2059a4870f?s=39&d=identicon&r=g)[Jessica Hullman](http://users.eecs.northwestern.edu/~jhullman/) on [January 19, 2025 6:30 PM at 6:30 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388020) said:
        
        Fair point that loans are usually granted by for-profit institutions.
        
        [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2388020#respond)
        
4. ![](https://secure.gravatar.com/avatar/?s=68&d=identicon&r=g)Anonymous on [January 19, 2025 10:02 AM at 10:02 am](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2387969) said:
    
    In the last few decades there have been innumerable efforts to change the basis of decision making from profit to [insert belief here]. The results are in:
    
    [https://www.npr.org/2025/01/17/g-s1-43268/fire-battery-storage-plant-california-moss-landing](https://www.npr.org/2025/01/17/g-s1-43268/fire-battery-storage-plant-california-moss-landing)
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2387969#respond)
    
5. ![](https://secure.gravatar.com/avatar/087d4b749e60debf59b5e01898364a91?s=68&d=identicon&r=g)[Christian Hennig](https://www.unibo.it/sitoweb/christian.hennig/en) on [January 24, 2025 12:00 PM at 12:00 pm](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/#comment-2388284) said:
    
    I’m too late to the party once more, but anyway, a few thoughts here. It makes sense to distinguish probability interpretations into epistemic and aleatory, where frequentism is just one version of an aleatory interpretation. Particularly, in the philosophical literature there are several versions of propensity interpretations of probability, with a distinction between single case and long run propensities. The essence of aleatory interpretations of probability is that the probability is intrinsic to the “random experiment”, i.e., the situation or setup in which an outcome can be observed, and does not regard a state of information and potentially an individual.
    
    Now it is hard to tell what a propensity actually refers to if not a limiting relative frequency under infinite repetition. However we need to acknowledge that infinite identical repetition of experiments does not really exist, and this concerns infinity as well as the “identical repetition” (de Finetti wrote that whatever can be distinguished cannot be truly identical). Note also, as additional complication, that we should distinguish between i.i.d. repetition of random experiments, and the kind of identical repetition that is required for the definition of frequentist probability. An i.i.d. random sequence is a sequence in which probabilities are assigned to possible outcomes of the whole sequence, and in order to interpret those in a frequentist manner, *the whole sequence* needs to be identically repeated (and can’t serve as a sequence to define the probability for an outcome in a single component)!
    
    The baseline of this is that infinite repetitions are not real facts but thought constructs that help to clarify the thinking behind interpreting probabilities as referring to real random experiments rather than states of information and belief. But it doesn’t make sense to demand that such repetitions really exist. Of course, if something exists that looks very much like many identical repetitions (even though indeed it isn’t), frequentist and actually general aleatory thinking seems to align better with observable reality than if this isn’t the case, but in principle the thought construct of infinite repetition can be applied very generally, even to a specific individual given all kinds of information including that any real repetition is obviously not identical because what happened earlier will affect what happens later, or for other reasons relating to the fact that the world won’t stand still.
    
    This blurs the distinction between frequentist and propensity versions of aleatory probability (I often catch myself not distinguishing properly between them and in particular calling something “frequentist” than should probably better be called “propensity” but may in fact be a thing in between these), and to some extent also between these and personal epistemic probabilities, because the frequentist would have a hard time to assign “objectivity” to the choice of an artificial thought construct and its implications. Being a constructivist myself, however, I wouldn’t hold this against frequentism/aleatory probability; there is no scientific modelling without artificial thought constructs, and as long as it helps us to achieve something, why not? Also, in this way, I have no issues with thinking about aleatory (or even frequentist) probabilities in singular situations; the probability is constructed by embedding it into a thought experiment. The problem is, for me, not philosophical but practical – if the thought experiment doesn’t have a convincing link to reality in the specific situation of interest, we may not assign much meaning to it. However statistical methodology offers tools such as interpreting residuals from models in a frequentist way, which we think of as repeatable even if every single observation (defined by a high dimensional x-vector in a regression, say) isn’t.
    
    Exchangeability is such a thought construct as well. It is well known that if Bayes is taken literally, once a sequence of experiments is taken as exchangeable, there are no possible outcomes that can get the modeller out of the exchangeability assumption, and this consequence would make exchangeability grossly unattractive and in fact unrealistic regarding real people’s thinking of real sequences. However, exchangeability is a great modelling tool if used temporarily with the license to drop it in the face of evidence that indicates against it (one could interpret this as saying that aleatory events disproves the model, or, from a fully epistemic point of view, that it shows that exchangeability wasn’t really what we believed in the first place), even if this violates standard Bayesian reasoning. Which is how we should treat our artificial thought constructs indeed.
    
    The mathematical fact that assuming exchangeability amounts to believing in a limiting frequency that can have a frequentist interpretation is in the first place a nice implication of both Bayesian and frequentist thought constructs. I’m comfortable to operate with such thought constructs as what they are; their use and benefit in my view is not determined by considerations whether in any given situation such assumptions and “existence claims” are “really true” or not. This in particular means that for me situations in which there is obviously no “real identical repetition” can still be interpreted in a frequentist way and also modelled involving exchangeability, as long as we are aware that reality is not (quite) what the model implies, and the model helps us anyway.
    
    [Reply ↓](https://statmodeling.stat.columbia.edu/2025/01/17/how-far-can-exchangeability-get-us-toward-agreeing-on-individual-probability/?replytocom=2388284#respond)



