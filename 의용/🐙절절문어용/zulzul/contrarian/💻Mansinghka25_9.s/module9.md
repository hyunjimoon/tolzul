2025-04-22

scaling 3d scene perception using prob.prog

pixels and images ()

structured problem - raw visual data to 3d representations

localize and navigate - interdependent object - interact with each of them 

general purpose robots - computer graphics (generating , manipulating, psnr to evalute photorealism)
# computer graph
due to optimized for photo realism -> computationally costly and slow; doesn't capture scence uncertainty - many scences representing

# computer vision

learning function to predict ; costly to train and struggle out of distribution (can't generalize)

# robotics
3d perception to enable real-world action selection,  -> modular pipelines ar inconsiste; globsally coherence uncertainty over scences - can't generalize long tail 

lesely's iew - real world 

---
probabilistic modeling of multi resolution latent 3d worlds
real world (variability), data (incomplete), models (approximate), tasks (uncertainty)

---
principled framwork to vaiable

genrative 3d graphics program (perception as inverse graphics - decomposed to each modules)

---
3dp3 - (faster)> bayes3d  -(multi reolution, tracks)-> gen3d; can be applied to open world

violate basic common sense failure

latent 3d scence, observed image p(z,x) = p(z) * p(x|z)

prior on latent scence -> model compositionaly - coarse voxel models; distributions on the 3d bianry

learn shape distribution from data (five images)
p(x|z)

underlying depence btw ; table -> p1,2,3,4,5 (setting in contact with table)

paraent

uniform over latent hypothesis

rendered point and observed (n by m distrance) -> spherse prioabilty falls off to zero -> shich spere

tolerate mistmatch the point cloud 

🙋‍♀️is this idea related to adding independent noise makes smooths out distribution and makes conditional distribution computable?

scne graph (involutive mcmc), scnec graph parameters (custom mcmc)

changing the structure of model, add edge; when no edge between bowl and sugar box (broad prior) -> prior on position is more restrited 
uniform over window 0 to 2, gaussian; pose prior is more constrated (concise represntation - occums's ; x,y,z - pose has six parmaeters whereas contact point has three parametesr)

implemented with cuda 

loglikelihood calculation - atomically (two different gaussian may be access the same)

Okay, let's think about the one Gaussian case in Gen three, if I had a model that's just like one Gaussian, then the things that are sampled from it are just, like a bunch of 3d points. If I sample IID from it, I'm just going to get a bunch of three points right. But if I now have one Gaussian here, and I render using this, this Gaussian flag model, when I shoot array like straight through that Gaussian, its depth and color will probably like match that Gaussian Exactly. But as I go like one pixel to the right, the way Gaussian spline works is like that Gaussian function falls off so it has less influence, and then you're interpolating between that weight function with that Gaussian and one minus that weight for the background. So as you get further and further away, the depth value that you're rendering like becomes the match. So I'm doing the scene from here, and the Gaussian is here. So imagine like a top down where a Gaussian is here. The rendered depth that will come out of this will look like,which is very odd, right? Because there you have these like, streaks of depth data that, like, shoot backwards from the sides of the Gaussians. But like, why does this not screw up Gaussian splatting? You think this would screw it up completely well, because they're not working in the one Gaussian like this. Fact that the shapes that are produced like look like this every time doesn't really matter if you're using millions of these Gaussians that, like, you can just chain them right next to each other and model a surface quite well.

comparing with foundationpose vision transformater

evaluate on low frame rate object pose tracking - 

---
takeaway
1. data is not a silver bullet (but models learned from enourous amounts of data still make common sense errors)
2. probability is not just about uncertainty (wee need that for robuts to work safely and efficiently and for av to uncerstand; coarse and approximat -> coarse to fine; variablilty of the world)
3. efficient and interprtable genai; blackbox and expensive to train -> lightweight; interpretable structured geomtric represntation; modularly exteded and debugged

