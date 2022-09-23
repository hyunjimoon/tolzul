#simulation

Suppose you're in charge of managing logistics of goods. Your job is to identify how much goods needs to be moved every day, and supplying sufficient transportation so that the entire logistic chain doesn't suffer from a halt. You're not a god, so there's no way to exactly identify the process that generates the amount of goods per day.

Your first job is to first identify what the generating process is, and other factors involved. For example, you might know that some factors such as weather or the number of orders handled by a nearby Amazon warehouse, etc. might have an effect on the outcome. Using this information you may come up with a model, say a poisson regression, that may or may not explain the generating process. Remember that epistemic uncertainty means you can't be certain about it.
