**15.879 Bringing Data into Dynamic Models, Fall 2022**

**Assignment 5: Calibration and Different Optimization Algorithms**

**Due: 10/14/2022; This is a more involved assignment, start early!**

In this exercise we introduce the basic idea of calibration and go a bit deeper into optimization algorithms used for calibration. The primary goal is to conduct simple calibration: identifying parameter values that best match simulations and data for target variables. Formally, our calibration task can be defined as an optimization problem:

(1)

Here  is the vector of estimated parameters with lower (lb) and upper (ub) bounds, and  is a function of the distance between target data series (d) and their simulated counter-parts (s). One could define different distance functions for the purpose of matching the data and simulated outcomes. For this week’s assignment we will use the following distance function:  

(2)

Here  is the tth measurement (over time) for the ith target data series variable, and  is the simulated counter-part for that.  is an appropriate weight assigned to the gap between simulation and data for each target variable. For this week assume these weights are the inverse of variance for the target data variable:

(3)

The primary goal for this week is to solve the calibrate your model against synthetic data using different optimization algorithms and compare the performance of those algorithms in this task. Calibration is often the most computationally intensive step in your analysis workflow: each value of  needs to be calculated using the given value of . A typical calibration may take thousands to millions of such evaluations of , and therefore doing the calibration efficiently is very important. You should have already set up your Vensim to compile models which speeds up simulations by 2-10 times (See assignment 2).

  

**Quick Background on Optimization** 

The literature on optimization methods is vast and there are many different dimensions along which one can categorize algorithms. For our purposes this week we will focus on the following features of algorithms:

-   Local vs. global: The payoff function we minimize or maximize (in this case ) may be multi-modal, that is, it may have multiple local peaks/valleys. This is specially the case for larger optimization problems with nonlinear dynamics systems. Some algorithms focus on finding local peaks (valleys) on the performance landscape, while others seek to find the global peak. We are ultimately interested in finding the global peak, but that is a harder task than finding a local one; local algorithms may thus modularize the task, allowing the researcher to iterate between finding a local peak and re-starting the algorithm from a different point on the parameter space which allows one to find another local peak. Sufficient “re-starts” allows you to assess how common local peaks may be and finish search when appropriate. Global algorithms in contrast may explore a larger region of parameter space and expand/contract that region based on feedback from prior evaluations of different parameter combinations. 
-   Gradient-based vs. gradient free: The gradient of payoff function, e.g. how  changes with respect to each member of estimated parameter vector , is an informative concept for selecting more promising regions of the parameter space. In fact a large number of algorithms, such as gradient descent methods, leverage this information to choose successive parameter values. When analytical expressions for gradient are available, using those often adds value. In the absence of analytical solutions however, the calculation of gradient for a n-dimensional parameter space requires at least n+1 simulations, a potentially significant cost which may or may not be justified in light of the benefits. Other methods, such as golden section search, enables informed search without a gradient. Other methods, such as stochastic gradient descent, may utilize partial information on gradients more efficiently. 

Optimization algorithms may vary in efficiency by an order of magnitude or more (e.g. computations needed to get to a target performance). While hundreds of different optimization algorithms exist, there is limited understanding about the ones that best fit the type of optimization problems we deal with in calibrating SD models. For example, Vensim has one primary built-in optimization algorithm (Powell search; which is a local, gradient free method), along with variants of simulated annealing (again gradient free and largely local; that is also applicable for conducting Markov Chain Monte Carlo analysis). Comparing these with alternatives may offer opportunities to leverage better algorithms for calibration tasks. This assignment is focused on doing such comparison on your model.

-   Reminder: you should create single-click solutions for your assignments, writing the code that conducts all the required analysis, and creates all the required graphs and tables, with minimum manual adjustments. For this purpose you should leverage the platform(s) you built in the assignment 3. In practice writing the relevant code is iterative: you may manually conduct some analysis in Vensim until you know you are getting what you want, then automate that part in code, and continue.
-   Create a synthetic dataset as input to your calibrations. In doing so, choose an appropriate “saveper”, that is, the frequency with which data is saved (Vensim has a built-in parameter with this name which you can set programmatically or manually and in model settings). That frequency should be informed by the meaning of time units in the real world, for example, daily covid-19 data makes daily saveper realistic, where as many economic data series are released quarterly justifying the corresponding saveper. 
-   Define the payoff definition file (.vpd) that operationalizes the calibration optimization function discussed above in your model. In building the payoff you may use either the “Policy” or the “Calibration” setting in Vensim. If using the “Policy” setting you will need to build the additional structure corresponding to equation 2 (though note that you don’t need to calculate the sum over time, Vensim would do that by taking an integral over time). In using the “Policy” option make sure the payoff is only calculated in the time step when there is a data point available, e.g. using a function like:

“If then else (d_i<>:NA:, w_i*(d_i-s_i)^2, :NA:)”

Alternatively, you could use Vensim’s “Calibration” option in defining the .vpd file (https://www.vensim.com/documentation/ref_payoff.html) in which case you can use “Normal” distribution and adjust “weight”s that are 1 over standard deviation of data for the corresponding variable. In either case, make sure the reported payoffs are consistent with the sum you are expecting to get.

-   Define the optimization control file for your calibration in Vensim. This file includes two components: on the top the optimization algorithm’s settings are specified. After that, the list of estimated parameters and their bounds are provided. 
-   Use the Powell optimization method to find the best-fitting model parameters. Specifically, use the default optimization options for the optimizer, with the following change: Choose “RRandom” for “Multiple Start” option; try 100 restarts (“:Restart_MAX=100”) of the optimizer from different points of the parameter space. Write a piece of code to parse the “.log” file coming out of the optimization (a sample code in matlab is provided; you probably need the equivalent in python), and figure out if different restarts are landing on the same, or different, local optima. This is an important diagnostic to decide if your optimization problem has many local optima (and thus requires more restarts), or not. 

Report your setup and findings from this exercise: how many target variables, how many data points for each, how many estimated parameters; as well as the computational costs for your calibration (how many simulations were needed to complete the search; that you can find from the .out file; along with the computation time on your machine; make sure you clock that programmatically). Also compare the estimated parameters against the ground truth in a table. How good is the fit?

-   Now, compare the two optimization methods in Vensim (Powell and MCMC/Simulated Annealing). Based on your experience from previous step, set a total number of simulations you think is enough for Powell optimizer to estimate the parameters (use Max Sims option in voc setting). The equivalent control parameter for simulated annealing is :MCLIMIT; so make sure the two are the same. Set other parameters of Simulated Annealing control based on your understanding of those. You may report results from a few comparative MCMC options that change those options as well. Another fruitful analysis is to repeat the comparison with 10 times more/fewer simulations. Based on these explorations comment on the relative effectiveness of the two methods in Vensim for the purpose of your calibration and summarize evidence to justify your conclusions.

  

**Beyond optimization in Vensim**

The optimization algorithms in Vensim are limited to two, so it is hard to know if you could do better with alternative algorithms, e.g. some of those from this week’s reading. Many different “solver” packages are available both open source and commercially; they vary in their focus areas, coverage of algorithms, and efficiency. A review of those alternatives is beyond the scope of this assignment, rather, we will focus on utilizing algorithms available in one such package, scipy.optimize. You are welcome to try alternatives if you feel adventurous, for example Matlab includes two optimization packages that offer a large number of alternative algorithms, but would require connecting Vensim to Matlab rather than Paython. Two general approaches could be used to utilize alternative algorithms. First, you could conduct the simulations inside the environment where you do your optimization (e.g. python), or you could continue to use Vensim and pass the payoff function from each simulation to python using a DLL call. The first method benefits from easier integration and lower communication overhead in function calls, but requires moving your model into python and simulations in python are often slower than compiled Vensim simulations. The second method’s downside is the slower communication between Vensim and python in passing parameters/payoff values. These methods map directly to alternative implementations you have worked on in assignment 3.

-   Set up your simulation/connection method and optimization package of choice, and compare at least 3 algorithms available through a different environment with those in Vensim. You may compare the methods by focusing on the change in payoff function for your calibration over different numbers of function call. Other alternative measures may include CPU time needed to get to a local optima, or the global one. Design and justify metrics for a fair comparison between different algorithms, conduct the experiments, and share your results. 

  

**Presentation**

For your presentation focus on sharing the insights you have gained from conducting calibration on synthetic data and comparing alternative optimization algorithms inside and outside Vensim.

  

Appendix- Matlab Function for parsing optimization logs

_function [payoffs,params]=ParsePayoffLogs(fname)_

  

_global drvNm_

_%% parsing the log file for payoffs_

_%% fname is the name of the text file (.log) to be parsed_

_%% payoffs is the list of payoffs achieved from different start points_

_%% params is the values of parameters corresponding to each start point_

  

_x=[];_

_fid=fopen([drvNm fname]);_

_maxp=0;_

_flt=1;_

_tline=fgetl(fid);_

_i=0;_

_while ischar(tline)_

_% this is the signature for a new search_

    _if not(isempty(strfind(tline,'This Search                   Pass 1      Final       .')))_

        _maxp=1;_

        _k=1;_

        _i=i+1;_

    _else_

        _if maxp==1 && (isempty(strfind(tline,'Simulations')) && isempty(strfind(tline,'Iterations')))_

            _[~,nomatch]=regexp(tline,'\s+(\t|\s\.)','match','split');_

            _y(i,k)=str2double(nomatch{end-1});_

            _k=k+1;_

        _end_

        _if maxp==1 && not(isempty(strfind(tline,'Payoff')))_

            _[~,nomatch]=regexp(tline,'\s+(\t|\s\.)','match','split');_

            _x(i)=str2double(nomatch{end-1});_

            _maxp=0;_

        _end_

        _if not(isempty(strfind(tline,'Floating point error during optimization with')))_

            _tline=fgetl(fid);_

            _tline=fgetl(fid);_

            _f=fopen([drvNm 'floating_' num2str(flt) '.cin'],'w');_

            _while (isempty(strfind(tline,'----------')));_

                _fprintf(f,'%s\r\n',tline(3:end));_

                _tline=fgetl(fid);_

            _end_

            _flt=flt+1;_

            _fclose(f);_

        _end_

    _end_

    _tline=fgetl(fid);_

_end_

_fclose(fid);_

  

  

_payoffs=x;_

_params=y;_

_end_