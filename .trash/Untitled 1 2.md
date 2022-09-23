
## big picture.
What?
- Data:
-- borders bookstore(bankrupt in early 2000s), 266 stores is their operations on a multivariate features (4 years)

- Model: system dynamics and hierarchical parameter estimation
- variables: turnover
How?
Why? 

And the data comes from a few and resource side from which is kind of turnover at hiring and so on, the data comes from operations things like inventory inventory turnover and from quality measures, so they have customer service and customer satisfaction surveys and so on.


 profitability for cleanliness or gluttonous, so there is something in the order of.

11
29.55049.380
 Altogether, for the different time series for each store over time, with different frequencies, some of them are monthly some of them are quarterly we may have a couple of items that are every six months, and maybe so that's kind of the type of data that we have.

12
50.79053.010
 This data we can go into more detail.

13
54.06002:11.940
 Then there is model right the model is it fairly generic aggregate model office stores operations which takes about Okay, you have a number of employees, they have a quality measure of sorts built.

14
02:14.40002:22.050
 around them, they have capabilities that is quality of organizational processes so.

15
02:22.68002:31.890
 How many employees, you have what is their capability level, what is the quality level comes together create something that we call it service capacity.

16
02:32.58002:50.550
 That service capacity, then compared to the demand you're getting leads to the sales you get in the store and part of it is kind of sales in terms of the number of people you serve versus how much each person buys and.

17
02:51.93003:11.670
 How many items they buy, and we have data for those separately, so we want to make those so the model makes those connections that the more service capacity, you have the better, you can serve a given number of customers, the more satisfied your customers, the more workers get a positive.

18
03:13.59003:25.110
 interaction they get more satisfied, the more the higher the quality of service, the more likely these people come back, so there is a feedback to demand.

19
03:25.62003:32.040
 And the better the quality of the work environment in terms of the quality of colleagues, the more likely, you can.

20
03:32.52003:40.440
 maintain high quality employees, so all of these are mechanisms that we qualitatively had heard about me that I thought the size.


03:40.74003:53.250
 In the literature, but bringing them together in a single setting all of these interacting pieces has not happened in the past, so in the paper you sent me that hasn't been published.

22
03:54.66003:58.830
 There was some estimation going on, yes, but.

23
04:00.15004:07.230
 The like a problem hidden variables or an observable variables have not yet been on it so.

24
04:08.25004:11.040
 So essentially what we want to do is to.

25
04:13.26004:29.340
 reward that paper, so this is that's the goal, so what you have seen in that paper is very similar to what we want to do, the problem with that paper, the way it was is that that estimation passenger essentially broke down.

26
04:30.87004:42.600
 Because, because when I was doing validation testing, so you can estimate anything and then hope that it is working, but you don't know whether it is working.

27
04:43.74005:01.980
 So when I created some synthetic data using the model as the engine yeah and then try to estimate the parameters of the model, using the method, I was using I wasn't getting reliable estimates and optimization algorithm for estimation converge two different local peaks.

28
05:03.39005:13.500
 Even if I started from the optimal from the true value that wouldn't find it so it is not just that that it is there is a problem with finding the.

29
05:14.16005:28.500
 P that so those things I at that time, essentially, I so it was before my tenure, I decided this is, and I already have spent a full year on this project, it is becoming too risky.

30
05:28.98005:38.790
 i'm not even sure if it can be scary yes and I don't have enough time to finish this get it published in time for my tenure so i'll come back to it.

31
05:39.005:52.290
 Later, so now i'm coming back to it great, so in that sense not now so that that that's the big picture and more specific technical issue yeah I was younger I was using.

32
05:52.86006:10.440
 Extended calm and filtering I don't know if you're familiar at all with the concept or not, if not that's okay yeah you don't have to be because short explanation right now i'm converging or deciding that maybe I don't even need the extent that content filtering.

33
06:11.52006:.720
 Because some kind of simpler experiments that I ran on the synthetic data suggests that without home and filtering I may get better results.

34
06:22.29006:29.940
 Which is great, because the common filtering increases computational cost significantly has other challenges that come with it so.

35
06:30.72006:49.140
 What we want to do now is to do the validation is step to make sure we can actually get meaningful reliable estimates using not without using extended comment filtering but addressing a few other technical issues.

36
06:50.52006:51.690
 If we succeed.

37
06:52.89007:00.660
 Then we will apply the same method to their actual data, rather than the synthetic data.

38
07:02.19007:06.480
 So that's the big picture of the where we are headed.

39
07:07.71007:09.300
 yeah so.

40
07:13.74007:22.980
 You produce synthetic data, so the common filtering framework and something we were introduced you briefly.

41
07:24.63007:25.950
 Extended common.

42
07:27.00007:28.140
 sense we don't need to worry about that.

43
07:30.00007:34.500
 Extended part of it is very useful just nonlinear system right.

44
07:36.12007:38.850
 I guess the part i'm struggling with is like.

45
07:40.35007:44.070
 You have some you have some true process like yeah.

46
07:45.24007:53.670
 The world yep and then you have a model, you know and what's the goal, the goal is to see if our model like.

47
07:54.72008:00.0
 We want to show that the model approximates this process that's exists in real life.

48
08:01.23008:01.770
 So.

49
08:03.99008:04.620
 Are we.

50
08:05.94008:07.440
 taking synthetic data.

51
08:09.30008:10.230
 From the model.

52
08:12.36008:12.900
 So.

53
08:13.95008:27.510
 Essentially kind of the real world yeah the real world is always different from any mom of course that's, by definition, but pretty much every statistical approach says, assuming that the model.

54
08:28.17008:37.740
 Is a good representation of the real world and we will go ahead and estimate this model and come up with parameter values.

55
08:38.37008:48.780
 Structural features that will then inform some relationships in the real world, that is, if we assume the models for yeah that's the general approach in pretty much any.

56
08:49.32009:05.280
 Now, in this case we have we are going to be the same process you're making a bunch of assumptions about what the real world looks like in a simplified version of it, which would be our oh yeah and and we can estimate that model but.

57
09:06.48009:12.840
 The step that is problematic, right now, what we are focusing on in the validation synthetic data is saying okay.

58
09:13.95009:27.660
 Even if I assume that the world is like my devil I don't know that they're my estimation process passenger can find a true parameter values of the model, so let me.

59
09:28.38009:43.440
 run the model as the real world, to generate some data that I hide the parameters of that data from my eyes or if I see you I don't have those yes, I go to the process of estimation, just as a real role.

60
09:44.16009:50.370
 then see if I am able to find it amateur is up now, I know what they are, yes, this is.

61
09:52.08010:01.680
 Familiar yes so that's a step, this is a fairly standard process is not universal but I guess pretty calm, do you simulate the data and.

62
10:02.49010:08.700
 That data and then by feeding that data can I recover the records that are know that I know are the.

63
10:09.33010:17.940
 ground troops yeah so essentially a way of creating ground truth, so that you can deal yeah that's cool and yeah that's me.

64
10:18.66010:22.740
 Okay, so right now we have the real world data, I have a bunch of.

65
10:23.16010:34.950
 Synthetic data sets that I have created, we could create more during this it's fairly straightforward it's just one simulation they are the easiest part, of course, you need to make a bunch of assumptions about the underlying.

66
10:35.22010:42.270
 Noise processes that drive the system that are not captured in the boundary of the model so if.

67
10:42.81010:53.820
 and real if the data generation process that you're modeling if it was no history, it was all deterministic then them all always bill, you can always find the.

68
10:54.51011:08.790
 models, you have to really have a job yeah noisiness like a board is what makes it challenging to the one so we're still making noise assumptions so, even if we are able to you know approximate this synthetic data.

69
11:09.81011:14.340
 That data was produced with some assumption about the noise in the world, yes.

70
11:15.06011:26.730
 which in a sense, we should be careful that we shouldn't know in their estimation is stack too much about the noise process that is yeah and if we make a.

71
11:27.09011:35.940
 New boss too much information about that noise yes that's an unfair characterization of so Those are some of the things being assumptions Internet.

72
11:36.63011:45.450
 Yes, so some of it is playing into something so you can increase or decrease the noise level to see where when does your estimation framework breakdown so that's.

73
11:45.84011:56.460
 A useful thing to do, and all there is to make sure in the estimation process you don't have access to data you didn't happen so those of you want to be as fair as.

74
11:57.51012:15.930
 So that's the big picture, now we have the model we have the data we have some synthetic data to get started with Jeff and what we want to what you can work on is essentially creating the pipeline yep for destination yep.

75
12:17.55012:37.650
 To make it as automated and straightforward as possible that pipeline and we wanted to have also flexibility to test alternative ways of estimating, so there are some architectural choices for our estimation process that we can play with it and.

76
12:39.96012:41.130
 And then.

77
12:42.63012:46.980
 As much as possible automate that kind of articles that we want to get.

78
12:47.67012:57.180
 Out of that estimation process, so you can quickly decide okay this changing my architecture added value, let me stick to that this change it and add value.

79
12:57.60013:07.740
 And because otherwise the process of integrating true, it is a very messy prone to error process you're dealing with dozens of files and.

80
13:08.46013:22.080
 Setting changes and so that's organized and easily readable by someone potentially not me, yes, so that it doesn't just die when I leave yes exam all of those things are things I know how to do it.

81
13:24.00013:25.800
 And then the basic.

82
13:27.75013:36.240
 tools we will be using when some is our simulation software yeah and not just because we are familiar with, but because when Sim.

83
13:37.05013:46.500
 can be compiled into c++ code that is fairly efficient yeah so I have done enough comparisons with other alternatives that for the simulation of steps.

84
13:47.01013:57.780
 In destination yeah it is as good as it gets yeah pretty much I mean I David Keith was like Benson has a strong has a powerful.

85
13:58.62014:08.580
 simulation engine yeah which I wouldn't know by using it, because the crashes all the time, but yeah so we have access to and.

86
14:09.24014:12.390
 Besides having Benson itself, we have access to a parallel.

87
14:12.78014:23.340
 version of Benson for our internal research purposes, courtesy of men on our systems, this is something they don't have it publicly, they just use it for their own.

88
14:23.61014:32.100
 processes, they were kind enough to share it with us when we started some coding work anyway that engine and I had a server.

89
14:32.88014:43.650
 That is MIT slums computing resources it's not a big server but 48 cores at least gives you some additional capabilities that powerful engine that speeds up.

90
14:44.01014:59.490
 The iterations of learning about these alternatives so I just asked them to give you access to the server so you will soon have that access and then we can have a shared folder there that you can kind of work there, and we can all.

91
15:00.78015:02.700
 track and see how things are going.

92
15:04.20015:04.770
 let's see.

93
15:08.07015:08.610
 So.

94
15:10.98015:18.090
 What are we trying to so like what are we trying to estimate those model parameters you've in the every publish.

95
15:20.07015:32.400
 If for discussion purposes it's reduced down to two parameters test richness and compensation, but the actual model, as I think seven or so.

96
15:32.94015:47.970
 Many more parameters, yes, so we can we can now go into those details, so this is kind of hires of high level, now we can zoom into the specifics, so there are specifics about the model specifics about the.

97
15:48.51015:56.040
 estimation process in Benson that you probably have not been exposed to much maybe you have seen one or two examples a little bit.

98
15:57.06016:11.820
 Like yes oh Catholic simulations but I never asked me anything anything events so definitely that would be useful, then there is kind of how you automate the when Sim working with Python so some examples of that.

99
16:13.32016:18.690
 And then, how to bring all those together is kind of the steps by steps and.

100
16:19.53016:33.330
 So i'll try to cover the basics today yeah and show it on the screen, so that you have the recording of it yep and then you need to kind of spend some time getting into the details digested and then you will have questions, yes.

101
16:33.96016:49.680
 So that's what I had in mind right so let's get started with the first part First things first we have any can come here, yes, just because day absolutely, and so the first is.

102
16:51.90017:00.960
 So let me just show you so I have this folder structure that is messy you don't need to worry about the mess okay.

103
17:02.52017:.390
 i'll start with the latest version of this, so this model has been going through multiple iterations in 2017 18 and I was actually something was mostly 17 and I was working on this and kind of retaliate is where currently the model is.

104
17:23.52017:24.420
 and

105
17:25.47017:35.790
 The model is an empty file, so you can just open it in medicine and i'm going to open it in this vegan version of the manson, so there is this.

106
17:36.12017:52.320
 Parallel van same that has a user interface, that is a little bit outdated compared to the old version, and as we go through all this i'm going to create a folder for you, so that I can share with you later on, so let's call this.

107
17:55.35017:55.770
 Is.

108
17:56.82017:57.0
 here.

109
18:02.01018:05.250
 So here we can have sub folder.

110
18:07.50018:17.520
 Inside tools i'm going to put this current version of Branson so that you don't need to.

111
18:19.29018:38.070
 worry about that so it'll run it will run you don't need to install anything, this is built, so that it is just accept Okay, so if I go here open the sky, it will expire sometime in September that's Okay, for now, we have it.

112
18:39.15018:44.130
 It actually opens right now the model that we just had that just to make sure we.

113
18:45.30018:51.060
 Put the model in that place if you have access to you can go here and say.

114
18:52.38018:53.550
 Marbles

115
18:55.32018:58.110
 then go here and say return.

116
19:02.55019:09.960
 Just just get you set up and i'll put the lonesome model here.

117
19:16.26019:17.250
 fall so.

118
19:18.30019:20.160
 This is the latest version.

119
19:.57019:22.980
 things I have been working on.

120
19:25.62019:27.390
 So this is.

1
19:28.59019:30.540
 And then here.

122
19:31.83019:36.120
 To this new folder that you just created.

123
19:39.27019:39.960
 It opens.

124
19:41.55019:46.620
 So let's do a quick tour of what is inside the model.

125
19:47.85019:58.890
 So one of our we added new version helpful to add some commentary on what it, what are the changes and updates and this is kind of ad hoc way of capturing because.

126
20:00.90020:15.360
 So this first view is essentially the main view of the model, the main in the sense that most of the mechanisms are happening here and, as you can see it's a fairly simple model in the sense that it has actually just.

127
20:15.96020:.060
 kind of these two stock valuables of service capabilities employee quality.

128
20:.63020:29.550
 And even employees themselves are not an explicit a stock and the reason it is not an exclusive to start is not that the real world.

129
20:30.09020:33.660
 Its employees are not really start variable but.

130
20:34.32020:43.140
 Because I we I have enough good data on employees that they can essentially derive employees, based on data they don't need to.

131
20:43.41020:55.140
 it's not an object, you have the number of employees, you know, have the turnover, you have the hiring, so why even bother trying to get the number of employees right to sign in you have yeah.

132
20:55.830:06.810
 yeah it's not done so, in that sense, it can be driving there because it doesn't function those talk, I mean no it doesn't but.

133
:08.430:19.920
 Because, well, it is not a stock were able to talk, so in that sense it doesn't function as a stock, it does matter because some of the mechanisms are relevant related to employees so turnover.

134
:20.280:36.990
 There is the impact of a bunch of things on turnover, that we do care about, so there is the impact of local unemployment rate on turnover impact of satisfaction internal were so those things we want to estimate.

135
:38.910:49.410
 So I have turnover data and I estimate, based on the current number of employees and impact of satisfaction on turnover and local unemployment rate and so on.

136
:49.62022:01.710
 What would be the expected turnover rate yeah and I compare that with the actual turnover date so that becomes a source of estimation got essentially an error term that influence model parameters.

137
22:03.30022:15.990
 And then the mechanisms, you can look at here so service capabilities are not observable, it is a fairly kind of aggregate construct is equivalent to service capacity or release.

138
22:16.59022:23.280
 it's a little bit different so service capabilities, is about the quality of your processes.

139
22:23.88022:40.560
 So that that are your processes, the more efficient, you are so the for the same number of people, you will have more service capacity, and then we have that service capacity somewhere here I search service capacity.

140
22:41.70022:43.470
 Service capabilities.

141
22:48.30022:48.810
To call.

142
22:53.79022:55.860
 Yes, so this is.

143
22:58.26022:59.790
 Serious capacity.

144
23:01.44023:02.820
 So CS is for.

145
23:06.90023:16.080
 Service capacity of service, but I don't know what's the lockdown so maybe we can we can read within like reverse yeah we can do here, now that yeah so.

146
23:20.34023:41.730
 So you have a total number of employees it's often go to customer service, some of them go to building capability, so this is CSS customer service, and this is different from capability building so they're capable to building Labor goes and builds capabilities, the rest goes to.

147
23:43.65023:45.420
 Sarah service provision.

148
23:46.68023:49.500
 customer service Labor demand is this thing.

149
23:50.76024:06.870
 Yes, yes, late love to them and then so it creates a demand for customer service based on the current level of the demand the demand that is coming into the system.

150
24:07.74024:14.340
 And then you, so there is a demand for customer service, there is a demand for capability building yes.

151
24:14.82024:23.850
 And then you as a manager has to decide how loud and that's one of the key decisions yeah how much you emphasize building capabilities versus.

152
24:24.27024:31.770
 Serving customers and that has a free parameter that we want so priority for capability priority CAP is that parameter.

153
24:32.31024:45.540
 It says how much we are emphasizing capability and then versus your answer documents and, for this is a very parameter that gets estimated I mean it's priority CAP.

154
24:46.38024:54.960
 So we get to how we are so yeah basically this patent strategy decision exactly it's a choice that's being made an argument is like.

155
24:55.68025:05.670
 could be identified biases or areas in making that that's already got that yeah that's their choice that's it that's a key to your ethical construct here after kinda.

156
25:06.15025:15.840
 And, and then based on that demand versus how much Labor you have and that's total Labor you have is total employees, you have you allocate that using this.

157
25:16.62025:27.510
 Decision rule and you get capacity use for service which becomes essentially what is allocated to serving customers, given your current capabilities given.

158
25:27.93025:43.830
 Those parameters of tasks parishioners productivity of employees and all you have into production function this becomes their capacity that essentially goes to customers and that's capacity, then compared to the demand could create their quality of service.

159
25:45.75025:55.170
 That quality of service informs how many customers you serve so demand is the number of people who want to get served but not often may get served.

160
25:55.71026:13.020
 And then, if the quality of services, higher, you can have more units per customer, you will have more units sold and so on, so that's fairly straightforward total sales impacts profits.

161
26:14.28026:25.680
 Talk I can't read it, so this is cumulative units so sold, and the only reason is that we are tracking it until the flush said, because we have.

162
26:26.58026:37.740
 records of sales on quarterly or whatever unit, so we accumulate that and then flush it out so that her yes, so you can make a comparison comparison, be the data that you have this really cool.

163
26:39.00026:48.780
 And then profits is fairly straightforward total sales minus 12 all costs that come from the turnover costs when you have terminal where it is costly.

164
26:49.20026:53.880
 And we don't know how much Terry you need to turn over, but we can estimate that and.

165
26:54.18027:05.070
 Cost of employees, how much you pay them that comes from their salary, we actually have the compensation that we are paying them so that's that's a straight forward to a great extent and.

166
27:06.06027:20.820
 And you have the sales margin impact of employee quality on margins all of those can be estimate that this is, if I have better quality employees i'll be able to sell items with higher margins nothing's like.

167
27:.96027:35.700
 So these are the main pieces and then there are impacts on capable who building and capability loss Okay, the loyalty last time that is these organizational routines may get lost if employees are not attending to it or they're not.

168
27:35.97027:40.830
 Following program manager role and that depends on the quality of employees, you have so.

169
27:42.30027:53.190
 Employee quality average quality impacts capability last time and turnover impacts capable of the last time range employee okay.

170
27:55.17028:13.590
 So that's and then the employee quality gradually changes, based on partly how much you pay them how much they are learning, so there is a learning mechanism, so the longer the tenure, the more they have learned.

171
28:15.51028:16.500
 What is there.

172
28:18.75028:28.410
 Other death spiral dynamics that are getting captured are we leaving that away like what like if your employee if your average employee quality.

173
28:29.55028:40.380
 starts going down, then the next best employees are gonna say I you know, and I don't know work here, and we do have some of those so yeah we do have the impact of employee quality.

174
28:40.65028:47.820
 On attractiveness of jobs, and therefore the quality of employees, that you are getting in, so there is average income in.

175
28:48.81029:05.340
 Quality surround you reach yes, which gets feedback, but from indicated satisfaction, which gets feedback from average quality so that feedback is exactly part of it and souring increases incoming quality.

176
29:06.57029:13.290
 versus typical salary and then there is impact of what fills impact of.

177
29:15.03029:22.320
 customer satisfaction your impact of satisfaction very nice, so that those are a few of those exist.

178
29:25.20029:33.810
 And then the next view has some additional pieces of demand, which is another stock valuable here we're treating it as.

179
29:36.06029:39.870
 Somewhat exhaustive list, but there is an impact from.

180
29:41.16029:49.050
 Impact of employing quality on demand, so if you have higher quality employees that create a better interaction relationship.

181
29:49.41029:56.970
 With customers, people are more likely to come back and if impact of service quality on demand, the quality of services good, you may.

182
29:57.72030:08.250
 Get increased the demand and but then there is a kind of a baseline that this goes back towards that baseline, and so there are a couple of parameters to this entity.

183
30:09.30030:22.290
 So those are chief ideas in the model, then there is a whole machinery for getting data into the model and to use that data to drive the model.

184
30:22.71030:35.460
 Or to compare model predictions or model simulations against it, so those are the two ways data becomes useful so those two are these two variables one is data driving in.

185
30:36.06030:50.940
 This is the data that drives the model, you are not comparing it with the actual valuable you're not trying to estimate these you're using these as drivers of the model, so you for labeling it yeah I.

186
30:53.34031:00.330
 don't know how nice it is, but I have tried to actually highlight what they are here, because this is a multi dimensional construct.

187
31:00.75031:09.330
 So did you get any family it of itself scripts in Benson a little bit I know what they are yeah so no, no, so you will.

188
31:09.75031:18.420
 See subscription this model every variable you click on it so demand has subscript it is called sims.

189
31:18.90031:35.820
 sims in this case, think about them as a store different stores so as one to as 266 gives you the different stores and around yeah just it's just an array and if it is something subscribe to the sims it means it applies to all elements of that array and.

190
31:37.26031:50.220
 If I go in, I can go and Edit the array elements, so there is this subscript dialog box that I click on it, and then I can say Okay, I want to look at sense.

191
31:50.82032:00.180
 Right now, I can pull out, you can pull out a statistic wants to look at the graphs for it, you can edit the subscript So if I say, rather than 200 maybe 266.

192
32:00.78032:05.400
 Now I have the full sample if I want to do the analysis on a smaller subset.

193
32:05.88032:16.290
 I can actually just look at the 10 pounds 1010 stores by just going from one to 10 or just a specific sample that I want to you can randomly yeah you can run.

194
32:16.56032:29.070
 So, and only as well, so in the base case though we're simulating Carver ministers, that is to 66 in parallel independently, yes, right now, in parallel, not completely independent will get to the independent stick.

195
32:30.39032:48.900
 i'm using 200,000,266 for some constitutional reason that I don't fully understand when we get to to 66 cents in parallel engine does not do anything power it gets overwhelmed with the number of parameters seminar i've asked those guys what's happening, this alone what they'll say.

196
32:51.48033:09.030
 hey if we can get there, so that and then, if you go into this data driving in you see it is actually sub scripted by two indices one is sims for different stories and then Dr b's for different elements of this data.

197
33:10.20033:17.700
 series yeah and those elements V1 to we  our actual payroll fan payroll.

198
33:18.81033:19.530
 Full.

199
33:20.73033:26.340
 Registered Count of employees waging 2001 and 2002.

200
33:28.50033:43.620
 part time registered count all managers can total compensation competition competition in the local area unemployment wage seasonality payroll seasonality SK use etc, etc season, the.

201
33:44.67033:45.240
 audience.

202
33:46.83034:01.080
 I think it is so we can actually look at the data so it's actually it's all V 11th so you can say okay let's go to this element of the rv and pick the 11.

203
34:03.18034:08.820
 And then go to data driving in for we'll see what do we see you.

204
34:10.14034:20.610
 have to first put some around to others, we are in a different folder so let me get some this comes here and.

205
34:25.92034:26.670
just call.

206
34:47.73034:58.260
 We also put the things we need for being able to do some calculations so orders data stats borders data and then this.

207
34:59.64035:02.430
 Is these are data for school.

208
35:13.14035:14.790
 they're not in the destination.

209
35:16.08035:27.390
 So somehow I had already collected selected the other ones just don't give me access to anything where I can delete files, though it, so I have a very good enough for between summer OK.

0
35:30.87035:49.650
 OK, so now I selected this last simulation doesn't matter any of them, because this is data that is reads it doesn't yeah it doesn't need an energy, so this is a novelty factor partner, yes right So you see this V 11 yep it is essentially a set multiplier of sales that they expect.

1
35:51.06036:03.300
 In different monsters, and maybe a calculated it myself, based on the actual sales across all the stores and created an average factor that captures seasonality, so I think i'm just kind of fair.

2
36:03.78036:19.110
 And time based factor that allows for changes in demand so yeah we're not having store level like seasonality, not a separate store level is now what we have this global seasonality that.

3
36:19.98036:31.440
 applies to all the stores, because if you have a store level seasonality, then that captures all of the age, because for each store for each month, if you have a different.

4
36:32.43036:54.960
 input, then there is nothing left to explain terms of at least the demand side Okay, so you can see how these variables go into the system and and not every element of this may be relevant, but some of them are so, for example, you can go into the workforce variable and it is.

5
36:56.19037:02.640
 If it's if this variable is negative, then call it's not available, otherwise.

6
37:03.81037:06.930
 use this data driving into element 10 of it.

7
37:09.51037:20.160
 This is how you handle missing data, yes, part of it is for missing data and then need to interpolate between different pieces of data so that's kind of creates it.

8
37:20.70037:34.290
 So reading from that data than the workforce behavior looks like this and it's kind of probably meaningful for this specific store for a store one, the number of workforce has been changing like this.

9
37:36.72037:37.020
 Okay.

220
37:38.91037:54.960
 So these are data that goes into the simulation drivers to drive the simulation and then you have a separate set of 2020 or so data series that are things you try to match so actual sales actual profit.

2
37:56.82038:15.510
 turnover a full time total turnover off the part time people store manager return turnover for full value of inventory number of units sold number of units per transaction and actually this units is probably Unison damon three units sold as in its sole.

222
38:16.74038:19.800
 So the idea is, these are there yep.

223
38:20.40038:39.270
 And these are our models and now Jane between is the model so a typical regression has a bunch of these things that go in has a single one of these yeah and has a simple linear relationship here you have a messy dynamic model in the middle, you have a 20 dimensional our foods and.

224
38:40.53038:46.530
 The input of space is not that complex compared to other regressions in fact that's part of the.

225
38:47.55038:52.530
 appeal of this that you want to reduce the dimensionality ratio of the.

226
38:54.038:54.690
 So.

227
38:55.92039:08.040
 And essentially all of those data for Kelly, this is called data for calibration data for calorie, this is what is read again, this is a data data file, so, if you look at the equation, for it, it is data.

228
39:08.94039:24.090
 It is a raw data that it reads, there is no equation, and what when somebody sees an equation like this does says Oh, where should I go in with that data we tell that in the options in the simulation control menu.

229
39:25.11039:34.380
 In the advanced tab you list the data files, from which it should read these data series, in this case, this.

230
39:35.25039:52.320
 valley boys 100 ETF is there, I have stored their data for data for Keller and data driving this so just to understand the role of this yes.

231
39:53.01040:14.190
 This is the target we're trying to estimate, yes, so it contains real values or some personal values, all of these Nice, yes, as well as actually all of these days so everything is inside that fun, except for these three variables and one a and all one, these are.

232
40:15.54040:20.400
 These are related to turnover rates for.

233
40:22.08040:25.650
 Different types of employees full time part time and.

234
40:26.79040:43.560
 store manager, and these are again very over time, your averages across all the stores that change of that trend over time because I calculated them separately, over time, our side of.

235
40:45.42040:58.800
 The same I just use a different file and that these are saved in this other file that you saw here so that stats border data is the other files concept okay yeah there is a commerce that okay.

236
41:00.42041:14.430
 And then you can actually add, so the files that I just put it into our shared folder was here and there was a turd file, which is borders data, this is the actual data.

237
41:14.91041:27.330
 versus the vow point 100, which is the synthetic data, but that content in terms of that specific time services that are available are identical in terms of men, there is a data point for each store.

238
41:27.81041:36.300
 For each variable what the numbers would be different for all of these guys that you want to fit but are not different for these guys that are driving.

239
41:36.78041:46.140
 So that's how the structure of those two things, and you can always see oh I don't know what is in this media file, I want to see what is inside it, you can go to model.

240
41:46.53042:11.520
 and export the data set over you can select this vow boys or borders data, say, I want to export this and yeah some excel or top follow whatever and yeah we can just good so let's see do you want to override this no because it's going to a different location.

241
42:17.82042:18.690
 This is.

242
42:28.05042:29.670
 Yes, this so.

243
42:31.47042:40.890
 As you have experienced Benson is buggy, so I will go with the simpler thing, that is, in this case tap wanted to these books.

244
42:50.01042:52.980
 Even so, this time it's worked i've never been one of these fun.

245
42:55.05042:58.080
 yeah that's exactly so it's just a simple take.

246
42:59.76043:00.780
A look at this.

247
43:05.04043:.810
 So different times, these are monsters, this is the time units that we actually use in simulation and then data driving variable they only talk how about that yeah yeah very nice and should have.

248
43:22.89043:23.490
 here.

249
43:25.23043:39.150
 You should see data for cow and that's exactly those two variables that yeah I don't think it has many more, and you can see, so some some of these are every year or every six months, some of these are every months for each.

250
43:40.41043:42.390
 very, very helpful makes it concrete.

251
43:46.23043:46.530
Okay.

252
43:50.10044:10.080
 So that's the data yeah, then the data comes in, it is transfer, so there is kind of a place that I get the valuables in the model and turn them into a single sub scripted variable Sim out raw is that variable so you go into this valuable.

253
44:12.54044:25.260
 To its equations it says, the first element that is D one because you have different element, or something over the source, yes i'm essentially mapping into actual model variable so the total sales is the one.

254
44:26.76044:29.940
 You see, actual sales, yes, yes, so.

255
44:30.57044:38.160
 My understanding it correctly, you are taking, do you want across all 200 stores selling them, no, no, no, so.

256
44:38.37044:48.360
 This is just creating a valuable that is called Sim outer ah OK that's rather than having a single dimension has two dimensions okay one dimension is the store.

257
44:48.69044:58.710
 and the other is the type of data or which wich calm, which call yeah and that's column thing i'm in here, defining it, so the one.

258
44:59.61045:10.830
 Is reads the total sales that are simulated and then you can go to the next equation D to his profits and D3 is not as a placeholder so i'm pulling it.

259
45:11.16045:20.640
 Up holder, so that if I needed something else I could actually put it here, and so you want us to isolate the simulated.

260
45:.42045:36.180
 Sir, so the point is just a little bit computation not computational event and notation efficiency all i'm doing is rather than saying not compare profits with the first element of this.

261
45:37.17045:54.060
 Data series just yeah Just compare this valuable these two variables or both dimensions that's all we're speaking the same language, yes, so you can look at the elements here to see how they are created, but there is nothing really that to special.

262
45:55.44046:05.580
 Okay, and then that seem raw version becomes transformed, so these values are.

263
46:07.53046:.570
 Some of them you're directly observing so actual sales on directly objective for profit Center you know, some of them are variables inside the model that are not directly measured.

264
46:22.95046:30.810
 Rather, you have some kind of a messy measurement yeah that kind of relates to them, but are not exactly the same.

265
46:32.04046:36.540
 So this transformation process and.

266
46:37.65046:38.490
 says.

267
46:40.80046:41.790
 Okay, so.

268
46:43.77046:52.530
 This is for see this is for measure, act which is, which is directly measured measured indirect.

269
46:53.70046:59.070
 has its own noise and then current data is different, so this is.

270
47:00.69047:11.850
 for creating synthetic data I use this Similar trends and placeholder doesn't do anything so this one is not very formative see one.

271
47:12.54047:23.610
 So all that was happening in trance was adding noise to what to do, they're generating here you're transforming them by adding noise, yes, and then they turn.

272
47:25.98047:26.310
 See.

273
47:30.00047:30.540
 Something.

274
47:31.95047:35.970
 Is or anything it's preposterous community.

275
47:37.44047:58.380
 Oh, I missed this measured indirect So this is the key team not paid in the sense that it is a yes, it can come conceptually distinctive there is a whole set of Sub scripts that i'm calling the measure indirect and I can see what they are, by going into that subscript.

276
48:00.33048:20.430
 box yeah I go into the data and say okay what was measure indirect, these are these are these on it so for all of these, and I can edit those by clicking on these two quarters, these are the elements that are indirectly measure for those indirectly measured ones I have a very special.

277
48:.57048:23.970
 For relations, the formulation says.

278
48:25.17048:36.090
 Each indirectly measured item and, if you remember things like customer satisfaction yeah environment your customer service is a linear combination of my service capabilities.

279
48:38.01048:54.600
 With some weight my quality of service, with some weight and my average quality of employees with something Okay, plus some bias that shifts it from the baseline so I now have a bunch of parameters capability beat.

280
48:56.04049:01.380
 customer service rate and employee quality bait and this bias thing.

281
49:02.19049:14.970
 If I need to estimate, to see how they map into this specific valuable customer service interaction or customer service environment or customer service overall score or manager or.

282
49:15.36049:30.540
 Other things SS and all that which you have measures I have measures for those yeah I am not simulating them exclusively so, I am creating i'm saying, these are functions of these underlying concepts yeah so.

283
49:31.29049:41.940
 that's that's how I try to estimate map them and then is add a few more constraints in setting up my.

284
49:42.45049:51.630
 optimization by saying, for example, customer service may relate only to have these may may only relate to quality of service.

285
49:51.87049:59.280
 And average quality of employees, it may not be about service capability, so I would impose a value of zero on capability way.

286
49:59.91050:19.680
 When it comes into the value customer service, so you based on theory, yes, based on pure you create these constraints on the news bites depending on what you're trying to yes exactly and then all of these are allowed to go through a nonlinear.

287
50:22.08050:25.260
 transformation somewhere for me.

288
50:26.52050:27.540
 just trying to.

289
50:29.76050:30.810
 Do here I mean.

290
50:35.49050:38.820
 So then, it gets a noise for its measurement.

291
50:40.35050:40.920
 don't even.

292
50:42.30050:43.560
 add the non linearity.

293
50:45.96050:50.850
 I have enough degrees of freedom here with a baseline and then the transformation.

294
50:52.47051:11.850
 Okay, so now we are generating what we can measure we then can compare measurements with debt yeah so now, you have the backbone of what is happening here yeah now let's go talk about estimation creators, if you want to estimate this type of a model, what do you do well.

295
51:13.23051:23.100
 What is estimation is finding parameter values that minimize the gap between data and model some measure of that gap.

296
51:24.18051:37.770
 Now you can define a likelihood function to quantify that gap, you can do something more heuristic with least squares or something or absolute error so that's the big picture, certainly searching the parameter space for what me is that.

297
51:39.36051:47.970
 How do we approach it here while would define at Su the likelihood function is kind of a likelihood function with some assumptions.

298
51:49.35052:02.910
 Because livelihoods are very good for other purposes they really help us off days, so the likelihood function i'm defining is i'm thinking of all of these variables in two categories, the ones that are.

299
52:03.72052:.420
 integer comes specifically turnover and then the ones that are I can assume some normal distribution is OK approximation more the error term related to the are more continuous and that was the only thing you're like.

300
52:22.26052:34.050
 it's not a small car is creating So if I have one vs zero turnover assuming it is normal it's not a very good assumption, whereas if I have sales of a million versus.

301
52:35.25052:46.500
 my prediction in the model is 900 that's a good approximation, that the error time could be the norm So these are the two categories yeah and i'm creating.

302
52:47.10052:58.830
 pay off pieces for these two types one using a pulse on likelihood the other using a gaussian life is how you tell me this is around it, or having created.

303
52:59.37053:16.020
 Yes, yes, so the payoff says okay so ignore this if the now, so I mean what all it does is that when there is no data and calculating anything yeah then data for calibration, this is the data coming in.

304
53:18.60053:24.780
 This is the likelihood function for pass on distribution okay essentially.

305
53:25.38053:36.120
 This scenario i'd like to hear doing maximum one yeah i'm doing maximum life Okay, all it is doing is creating the error term for maximum likelihood by defining the log likelihood for costs on distribution.

306
53:36.39053:43.050
 Even the model that is predicting this rate and the events that are happening that's all that goes into this equation.

307
53:43.74054:06.0
 Similarly, the gaussian one same idea same idea, but this time with the normal distribution aerator so so the personas for the turnover and the gaussian service for everything, so these two are now creating things that I want to maximize i'm trying to maximize the log life yeah so.

308
54:07.74054:11.310
 Then I need to tell one seem to maximize these two guys yeah.

309
54:12.57054:17.340
 But by changing a bunch of things, and you have to tell which ones change exactly so.

310
54:18.54054:30.720
 What i'm telling it to change is all the parameters that are defined, here we have defined all these kinds of capabilities we are defining the all these effects of this thing on that tending.

311
54:31.23054:39.180
 a bunch of these parameters are global global in the sense that they equally apply to all the all the stores.

312
54:39.66054:48.090
 and, specifically, all these things about capable debates customer service faith and so on your, this is the same mapping from those underlying cause.

313
54:48.57054:56.040
 there's no dependence independence on the store so those things these parameters don't have any store subscript you go into them.

314
54:56.40055:15.480
 Is is just measure indirect it doesn't have any store subscribe yeah whereas I have parameter is related to hear demand return time or maybe effective quality on demand, you may argue this depends on the store effect of.

315
55:18.12055:25.740
 service quality on demand, you may argue it doesn't yes that's open question yeah and we could we want to be able to.

316
55:26.19055:34.710
 change that, depending on what we think is theoretically defensible so right now, it is subscribe to them, since, and right now, you can see, it is not actually.

317
55:35.10055:52.500
 A number rather itself is an equation So what is this equation doing so what we showed that can go to the this last view this is where i'm defining all of the parameters that our store base but could potentially be.

318
55:53.64056:00.750
 same across all the shows, so I call this so let's say sales margin is a parameter.

319
56:01.32056:15.360
 I may think they're all the same across different stores, or I may think it is a story specific So how do I switch between those two interpretations, if I think they're all the same across the stores, I have this parameter sales marketing of.

320
56:16.38056:17.370
 It is just another.

3
56:18.63056:31.200
 No subscript and so, if this applies to everyone if it's if it is determining sales margin, and then I have the alternative sales margin store that is specific to the sense.

322
56:31.56056:43.710
 Because it is a specific because it has this subscript it can get different values now if I put a single value here it'll it will assume, which is all the same for everybody, but in optimization, I can tell.

323
56:44.76056:46.200
 different values for different.

324
56:47.61056:57.270
 For different since building it this way, gives you that flexibility, yes, now now next the equation is what gives me the flexibility so sales margin, I say.

325
56:57.81057:16.650
 It is sales margin all that single parameter multiply by one minus this store level parameters for sales margin, this is their subscription within that so I have defined the new subscription range for each parameter.

326
57:18.24057:27.420
 So this is a storage if this which is one, then it becomes store level, and if it is zero it becomes global.

327
57:28.56057:47.220
 So, so you can now see everything is defined using this method, so now, I can just go here and say, rather than everything being one that is everything is store level, I wanted to be 1100, then I have to match for everything for now yeah.

328
57:49.17057:54.090
 yeah that's really short nd you could also create to.

329
57:55.65058:06.0
 solve saga ranges so right now, these are this is for the subscript range prior like calling it prior for reasons we'll get to in a second So these are.

330
58:08.79058:23.370
 or they're in the same order as these guys, so you can see initial demand initial employee quality other costs initial demand important quality other costs proper prior priority of capability.

331
58:24.45058:30.0
 EP turn over time is employee turnover time just this guy needs to go down on pure.

332
58:32.88058:33.750
 The right order.

333
58:38.70058:42.150
 So this is just so that it is vehicle easier to map them.

334
58:46.20059:05.700
 So this is the process for creating parameters that they can decide whether they want them to be store level mobile OK now let's say we want everything to be stored up for now, that is i'm putting one on the store level Paris for everything and then.

335
59:07.74059:20.220
 RD these independent across different stores or not that's the kind of important What if they are independent and giving a lot of degrees of freedom yeah for each store because essentially have 30 of.

336
59:.12059:29.520
 unrealistic it's a huge amount of flexibility and most likely the model fits the data perfectly or very well, but not for the right reason.

337
59:30.39059:43.200
 it's kind of overfit So what is the alternative One way is to reduce the number of these parameters and say okay only these four or five, and that was kind of the formulation we had in the version of the paper that you saw.

338
59:43.62059:59.910
 Only these four or five and one that I really believe are independent across the stores and then the rest are all the same across the stores, so that was that would be one day of doing it and that's why i've usually have separated them into these two chunks.

339
02.19011.160
 Another way that I have come up in the last couple of years with co with modeling and found to be useful, is to say, well.

340
12.18023.490
 They could be different, but it can't be two different So what does that mean it means that I have a prior on how far they can get from each other.

341
23.82037.320
 So for these parameters initial demand employee quality other calls priority if capability, maybe I let them to be more flexible to separate from each other more and for these parameters.

342
37.80046.620
 I want them to stay together closer together, so how do you implement that essentially add some additional penalty.

343
46.98059.430
 For being for being spread out So how do we implement that penalty it is essentially this prior error, there is a penalty here that says, I have a prior and how close these guys are together yeah.

344
00.06011.760
 And that is that this parameter absolute the standard deviation you use pencils, and this is essentially the standard deviation that for each of those.

345
13.26029.460
 These variables that I think is reasonable to see so for initial demand, this is the first element in our ordering $30,000 standard deviation across the stores for initial the turnout doll this.

346
30.51041.490
 Maybe I don't remember what it says it might might, it is the vm and sales like number of cells, so the third one is cost.

347
44.46050.820
 me see I think the man is in persons who visit the customers per year, or something or maybe four months.

348
52.86002:18.150
 Anyway, that is, the variance i'm Okay, with it, and then the further you get to variance of that parameter, the more European odds and i've used the square root type of a penalty here so that's kind of a little bit ad hoc you could turn this into a more formal.

349
02:19.17002:20.370
 basie and prior.

350
02:.78002:22.470
 penalty.

351
02:23.79002:41.730
 But for reasons we can get to this simple hack is a little bit better and easy to understand it's easy to understand, it is also you can easily change the number of stores and you don't need to change any of the equation that's, the main reason why I don't need so this can work with.

352
02:42.96002:44.820
 garbage my setup that's that's the reason.

353
02:45.90002:57.150
 What the numbers are kind of interpret double in terms of the Asian Asian prior and therefore they are after the comparable units with the other errors be having the rest of the model.

354
02:57.60003:01.050
 And therefore I can now create this whole livelihood thing.

355
03:01.62003:19.890
 That has the gaussian like you, who has the POs on likelihood it has this character likely who brings everything together into a single into a single Pam yes, so that single payoff let's just get the payoffs in place now, we need to get the vtt file so.

356
03:24.12003:44.490
 This is the payoff function when zoom users V PD so just add it here, and then, when soon optimization control V oC file is what controls the parameters that we want to calibrate over maintenance, so now let us see how you run an optimization.

357
03:46.62003:55.590
 You can start it from either the optimized menu or from the simulation control doesn't matter if you go to the simulation control.

358
03:56.22004:09.000
 You need to set up what is your path definition file you select the vtt file that you want, you can edit these big files in any text editor so that's a straightforward.

359
04:09.36004:15.810
 But you can also edit here, so if I select edit here, I can see that elements of the.

360
04:16.50004:32.730
 payoff So the first element is your definition my gaussian error term with the weight of one, which means I want to maximize it, so I don't change the way that I can I can give it a weight of higher or lower, but if I put a negative value monster me.

361
04:33.18004:43.770
 that's all that matters it's always traces it, that is, over time, it is cumulative looking at, so we can see how it's changing wrestling and once it's burned and we're happy.

362
04:44.07004:56.640
 So there is not any real burning here, because the simulation is the historical data is going to the time, but it is adding up all of those errors from the first month second month and third months together.

363
04:57.27005:04.050
 The underlying assumption is that those events or those error terms are independent from each other.

364
05:05.55005:18.720
 Which is common assumption, whether it works well or not, we need to test But OK so that's the Guardian one very similar one for the pass on one was on pay off later one.

365
05:19.95005:24.660
 always do it, that is, and then the last one is the priors error.

366
05:25.32005:38.220
 So this is probably our weight of negative one, because I have defined it to minimize that error and then this one only I want the value at the final time I don't want to get a penalty every time every time period.

367
05:39.06005:51.600
 I just want to make this better so that's it so you have the elements of debt payoff function, as I said, you could say just okay these you could open that file directly.

368
05:52.68005:53.190
 In.

369
05:54.78005:58.140
 Word processor or and no time.

370
05:59.52006:01.770
 notepad, and this is how it looks.

371
06:02.91006:09.510
 star P, is for policy, there is also a calibration option we are not using because.

372
06:11.25006:22.230
 This is more transparent, we know what's happening going into this House, so this is like our control exactly is a control code optimization and it gives you the option to.

373
06:22.86006:36.840
 programmatically change some of these things if you need yeah man, we probably don't need to change this specific file too much, but we could change it Okay, so I defined my power function now what should I define.

374
06:41.31006:48.000
 i'm trying to calibrate you, you want to you want to define your data your data your metrics against.

375
06:48.75006:54.0
 So the data is actually already the data that is measured against easy, as the hardy Ohio okay.

376
06:55.11007:05.220
 So the calibration is changing a bunch of parameters to minimize that or maximum liability purple you already set the parameters I haven't yet tell them which parameters a true champion.

377
07:05.67007:18.0
 So that's the next one, this is the optimization tonight it's just the next, and this optimization control V oC file is what we have here, you can again edited here.

378
07:19.86007:31.530
 We can go through the elements of this and or you can edit the text form, so the elements of this on the top is essentially the optimization engines path.

379
07:32.76007:45.870
 The basic default is OK, I normally don't change it, unless I see some reason to change it get the basic default users and optimization algorithm called Powell optimization it is.

380
07:46.35007:59.520
 kind of a gradient descent, but not exactly calculating the full gradient because that's very expensive in these higher dimensional parameters spaces, so it does kind of a little bit of an approximate gradient based on.

381
07:59.82008:08.160
 a bunch of recent trials and then does align searching the direction that is found, and the line search is a golden.

382
08:09.42008:16.770
 sections search method which is not exactly so it just cuts it into smaller pieces see what it finds.

383
08:18.27008:33.000
 It works it works i'm not claiming it is the best thing that is out there, but because it is built into Wednesday and it simplifies our life a lot, you do not only do the stochastic because normally when you have a problem, like this we do SPD.

384
08:34.23008:42.450
 that's not this so it isn't, it is not so it is not in the case in the sense that it doesn't.

385
08:43.62009:00.630
 So in the stochastic gradient descent, you are not calculating the full gradients right, you are doing a good job, setting a box in a ticket and in that sense, because, because it is also proximity can be great and where we have some, it is a good, yes, like a linear ization yeah.

386
09:02.28009:13.920
 Okay, so that anyway, we don't have that much option over it so that's what it is, you do have the option of using MC MC Markov chain Monte Carlo here so that you also.

387
09:14.52009:32.250
 Essentially you're doing an MC MC so you map the parameter Bible parameter regions, rather than just finding the peak of the Powell optimizer is to find a peek and cmc for hunting down search interface, and then down here is all the parameters, you want to check.

388
09:33.36009:44.310
 Okay, so every parameter here is so this one is initial demand the store this thing that we talked about yeah and one that was 30,000.

389
09:44.82009:51.180
 Yes, and this is the same as version that is story specific version yeah, as we said we want this to be story specific.

390
09:51.60010:08.310
 If I wanted this to be only for all, I would use enough demand all and it wouldn't have a seems subscribe to make sense and and how do you modify that was so you just add Clinton to drop or edited here directly so.

391
10:09.33010:17.580
 yeah so you're still liked you just give them boundaries minimum and maximum and you don't have to but it's a good idea to get boundaries, otherwise.

392
10:18.36010:26.850
 yeah it goes minus 10 to the power of six two plus 10 to the power of six for most parameters it's too much, when we look, we know it's not.

393
10:27.010:44.610
 yeah so it reduces the meaningful resolution of that step sizes in the optimization engine, so it doesn't do fine tuning, because it has a fractional tolerance of this much so that's it or you can I chose that you can you can make it.

394
10:45.84010:59.520
 more sensitive there again for crack if you have good bombs, this is a decent fractional tolerance OK so again, you could edit that directly, you could come here and Edit wc file.

395
11:01.59011:14.940
 And this is all of the top ones that have sins in them up to here are these guys that we have on this view, and then the rest are things that are global.

396
11:15.72011:33.180
 That is not specific to specific the stores and that's The rest is there a divider or no okay yeah you could mix them up, I just like to keep them clean yeah so that it's easier to fall Okay, so now we have defined the store level.

397
11:34.41011:48.240
 All of the parameters of the off number and how to be there, trying to optimize our you have defined a Pal function, so we are pretty ready to running and optimization so we can actually click optimize and see what happens.

398
11:50.97011:51.480
 yeah.

399
11:53.22012:07.170
 first thing OK, so now when Sim is compiling the model equations, this is the part that months in turns into a c++ code, so that it is running faster three to 10 times faster than running it without on violation so we're doing.

400
12:08.64012:09.180
 or.

401
12:11.28012:14.550
 Oh, there is a ci and file that I should add here so.

402
12:16.02012:22.350
 Do I have to tell it compiler it automatically i'll show you that in a SEC okay so.

403
12:31.77012:38.880
 I just want to buy it's three positive you have it's Okay, no that's other meeting didn't come true, so if you have to go, we can stop.

404
12:39.51012:52.320
 we're making I mean, I want to keep going I was planning on taking a 4pm flight, I think, oh flight, I think I can push it to divide um let's not do that let's let's get you to your flight so i'm having fun.

405
12:54.30012:57.720
 So i'll share this with you Okay, and then.

406
12:58.89013:09.960
 You need to kind of go through some of the details, so this last step you just push play and hopefully yeah or optimize optimize here, and it should do the trick.

407
13:10.59013:30.390
 Do I have to see Am I am vital I added the ci and file yeah, so now it is doing optimizations and it is dead best payoff is this much and it continues we're trying to maximize yes, so it creates a payoff that then its maximum Okay, which is.

408
13:31.62013:35.250
 Not the Prophet like when when you showed that.

409
13:36.63013:38.970
 Connor plot in class.

410
13:40.53013:51.360
 that's profit so we're that's not what's being optimized here, obviously, no, no, this is fitting the case data and then this is maximizing the life.

411
13:51.87013:58.710
 Right right right and then, once you have those parameters you simulate and you can all we can talk about how to make a robot later.

412
13:59.01014:15.600
 yeah those things don't worry about, but as as the curiosity like you get the parameters, then you run the model and profitability falls out of that yeah profitable to simulate it automatically yes, this one step Okay, you need to the so homework.

413
14:17.58014:26.280
 Where to start yes understand what is happening with the all the things that we talk because it takes time yeah and and then.

414
14:27.18014:33.450
 I think that would be good enough, a homework for this week, you need to understand how all these pieces come together.

415
14:33.72014:48.090
 i'll send you some information on compiling Okay, so that you can set it up on your own machine as well, and the one that is the server that we have already does the compiling but so that you know, having how to play with the equation.

416
14:50.01015:02.640
 Great, this is a good homework assignment when we meet next i'm around the schedule let's have some routines summer meeting time how about and it won't be a pattern of having a flight right.

417
15:05.64015:08.490
 Okay, the first one.

418
15:10.65015:11.640
 So let's see.

419
15:13.20015:22.860
 Here today's busy next week is busy i'm just looking at a couple of weeks, just to have a feel for what days are potentially better.

420
15:40.50015:49.170
 yeah Monday wanted to works for me, my name yeah hurting it works well for the coming weeks.

4
15:51.12016:03.390
 step that next week, might now next week yeah let's let's do one they wanted to awesome using a calendar yeah awesome okay and yeah i'll be not having a plate, oh no worries.

422
16:03.99016:12.660
 Go go, you should go if you have any chance of getting there 4pm yeah I you know I fly for free, so if I don't make it, though.

423
16:14.04016:15.600
 Okay that's good good.

424
16:16.80016:19.890
 This is very exciting, thank you for taking the time to walk me through.

425
16:22.74016:23.340
 Next week.

426
16:24.51016:31.440
 i'll have some more understanding and then we can start I guess yeah and so like into kind of.

427
16:32.79016:36.750
 a ton of stuff yeah got together yeah.

428
16:39.42016:39.780
 No.

429
16:40.95016:43.800
 It shouldn't be that this is a lot so.

 We sent me the zoom recording yes absolutely and that's when I forget your bag, and let me stop recording 

