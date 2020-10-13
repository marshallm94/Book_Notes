[TOC]

# Observation and Experiment: An Introduction to Causal Inference

[Book Link](https://www.amazon.com/Observation-Experiment-Introduction-Causal-Inference/dp/0674241630/ref=sr_1_1?crid=UQIIXTVGBIRX&dchild=1&keywords=observation+and+experiment+an+introduction+to+causal+inference&qid=1601735207&sprefix=Observation+and+ex%2Caps%2C157&sr=8-1)

## Unorganized Thoughts

* Quote (page 38): "People often want more than this from a test of a null
  hypothesis. They desire to know whether the hypothesis is true or false, not
  whether available data constitute strong evidence against the null hypothesis
  or else provide little guidance about its truth. This is a forlorn desire, for
  it is not hypothesis testing but the world itself that refuses to comply."
	* "Can you prove causality with statistics?"
		* Beyond **all doubt**, no; beyond **a reasonable doubt**,
		  absolutely.

* Quote (page 44): "It is an enormous, unforgivable mistake to interpret
  'accepting the null hypothesis' as providing evidence that the null
  hypothesis is true. 'Accepting a null hypothesis' means failing to provide
  much evidence about whether it is true or false."

## Chapter Summaries

### 1

* Randomized group assignment is integral to causal inference because it ensures
  that the observed covariates $X_i$ of patient $i$ have no affect on which group
  patient $i$ is assigned to, and more importantly, **it ensure that all
  unobserved covariates $U_i$ have no affect on which group patient $i$ is
  assigned to.**

### 2

* The causal effect of a treatment **can not** be determined for any one
  individual - if patient $i$ was assigned to the treatment group and had a
  favorable outcome, one can not know if that same patient $i$ would have had
  that same favorable outcome if they were assigned to the control group. This
  is the only way that one could determine causality for patient $i$. Since
  this is not possible (this is the definition of a counterfactual), causal
  inference is not possible on the individual level.

* The **average** causal effect of a treatment **can** be inferred -
  randomized group assignment allows an estimate of the average treatment effect
  and an estimate of the average control (no treatment) effect.

### 3

* Uniformity trial - An experiment (often ran in the 1920's and 1930's) where the
  distinction between treatment and control groups was retained, however **both
  groups received the same treatment (or both groups didn't receive
  treatment).** This allows one to think about one of the fundamental questions 
  of hypothesis testing, "What could we expect to happen that is due to chance
  variation?"
	* Typically used in an agricultural context to determine if fertilizer
	A was better than fertilizer B, a farm would be randomly divided into
	many plots and assign a plot to use either fertilizer A or B. **However,
	all plots were treated the same way (either fertilizer A or B) - giving
	the investigator an answer to the question, "What can be expected due to
	random variation?"


## Reasoning Checks

### Page 36: "There are 70 ways to pick $m = 4$ patients for treatment from $I = 8$."

**The Binomial Connection to Randomized Group Assignment**

Since order doesn't matter, the formula for combinations should be used: (the
group assignment vector [1,1,1,1,0,0,**0**,0] isn't materially different from
the group assignment vector [1,1,1,1,0,0,0,**0**]; the $7^{th}$ patient is still
in the control group (0) and the $8^{th}$ is still in the control group; moving
the **bold 0** doesn't change that fact), the formula for combinations should be
used:

$$

{n \choose k} = \frac{ n! }{ (n - k)! \cdot k! } = \frac{ 8! }{ (8 - 4)! \cdot
4! } = \frac{ 8! }{ 4! \cdot 4!} =

\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot \cancel{ 4 } \cdot \cancel{ 3 } \cdot
\cancel{2} \cdot \cancel{1}}{4 \cdot 3 \cdot 2 \cdot 1 \cdot \cancel{ 4 } \cdot
\cancel{ 3 } \cdot \cancel{2} \cdot \cancel{1}} =

\frac{ 1680 } { 24 } = 70

$$

This gives us the number of unique ways that 8 items can be arranged when order
doesn't matter. Referencing the context of the book, this also gives us the
"Treatment Indicators" section of table 3.2; this can be thought of as the
"Binary Manifestation of Possible Group Assignment Vectors". The subscript of
each number below indicates the patient ID, while the number 1 or 0 indicates if
patient $i$ was in the treatment group (1) or the control group (0).

$$

\left[ 1_1,1_2,1_3,1_4,0_5,0_6,0_7,0_8 \right] \\ \left[
1_1,1_2,1_3,0_4,1_5,0_6,0_7,0_8 \right] \\ \left[
1_1,1_2,1_3,0_4,0_5,1_6,0_7,0_8 \right] \\ \vdots \\ \left[
0_1,0_2,0_3,1_4,0_5,1_6,1_7,1_8 \right] \\ \left[
0_1,0_2,0_3,0_4,1_5,1_6,1_7,1_8 \right] \\

$$

Re-written to illustrate the the probabilistic underpinnings of the "Binary
Manifestation of Possible Group Assignment Vectors,", we get the "Probabilistic
Representation of Possible Group Assignment Vectors." (Note that since there is
an equal probability of being assigned a 1 or 0, $P = 1 - P = 0.5$. In order to
clearly show "which 0.5" I'm referring to, a **bold** $\pmb{0.5_i}$ will mean
that patient $i$ ended up in the control group (0), whereas a normal typeface
$0.5_i$ will indicate that patient $i$ ended up in the treatment group (1))

$$

\left[ 0.5_1,0.5_2,.0.5_3,0.5_4,\pmb{ 0.5_5 },\pmb{ 0.5_6 },\pmb{ 0.5_7 },\pmb{
0.5_8 } \right] \\ \left[ 0.5_1,0.5_2,.0.5_3,\pmb{ 0.5_4 },0.5_5,\pmb{ 0.5_6
},\pmb{ 0.5_7 },\pmb{ 0.5_8 } \right] \\ \left[ 0.5_1,0.5_2,.0.5_3,\pmb{ 0.5_4
},\pmb{ 0.5_5 },0.5_6,\pmb{ 0.5_7 },\pmb{ 0.5_8 } \right] \\ \vdots \\ \left[
\pmb{ 0.5_1 },\pmb{ 0.5_2 },.\pmb{ 0.5_3 },0.5_4,\pmb{ 0.5_5 },0.5_6,0.5_7,0.5_8
\right] \\ \left[ \pmb{ 0.5_1 },\pmb{ 0.5_2 },.\pmb{ 0.5_3 },\pmb{ 0.5_4
},0.5_5,0.5_6,0.5_7,0.5_8 \right] \\

$$

The above is the "expanded" version of the Binomial PMF (shown below) when $n =
8, k = 4, P = 0.5$. Reading this within the context of the book, this says
"There are 70 unique ways to arrange 4 $(0.5)$ terms and 4 $\pmb{0.5}$ terms."

$$
(70) ( 0.5 )^4 ( \pmb{ 0.5 } )^4
$$

Reading the above within the context of the Binomial PMF, this says, "The
probability that one observes $k = 4$ successes out of $n = 8$ independent trials
is equal to 0.27"

$$
\begin{align}

P(X = k) & = {n \choose k} ( P )^k (1 - P)^{n -k} \\
& = (70) ( 0.5 )^4 ( \pmb{ 0.5 } )^4 \\
& = (70) ( 0.5 )^8 \\
P(X = 4) & = 0.2734

\end{align}
$$

### Page 45 "Fisher's Exact Test; the 'Reasoned Bases for Inference'"

* "The word 'exact' means that the distribution in Table 3.5 is exactly the
  distribution of the test statistic $T$ in a completely randomized experiment
  when Fisher's null hypothesis is true. That is, Table 3.5 is exactly the null
  distribution of $T$, not an approximation to its null distribution."
	* Rosenbaum hints at the fact that distribution approximations are
	  usually okay and are widely used in statistics. However, if one can
	  avoid them, that is one assumption less to worry about being wrong.
	* 

### Page 271: "...Do high-level NICU's save more lives?"



* This is a question that is a clear example of the need to ensure that one is
  comparing two things that are indeed comparable. Right off the bat, I could
  see how an un-inquisitive investigator, if he did not use matching techniques,
  could come up with an answer of "No, high level NICU's do not save more lives.
  In fact, it appears that high level NICU's 'lose' more lives."
	* I think it is safe to assume that, if a mother and father know they
	  are going to have a baby born premature (perhaps with more
	  complications than a baby that is born less premature), they might go
	  out of their way to seek out a NICU with a higher rating. This could
	  then lead to the average acuity of babies in highly rated NICU's being
	  well above the average acuity of babies in lower rated NICU's.
	  Matching for acuity level (weeks premature, genetic complications,
	  etc) would be the minimum needed to ensure comparability.

### Page 272: "...The hope is that, having matched for many covariates, there is nothing special about mothers who live near or far from a hospital with a high-level NICU."

* Since the mothers in this study were matched for socioeconomic status, one
  shouldn't run into the problem of "Wealthier mothers might have to superior
  hospitals" - very important to match for this covariate.

There are "known known's" ($x_i$), there are "known unknown's" ($u_i$) and
finally the "Unknown unknown's" (covariates that you are completely unaware of
that might bias the outcome)

