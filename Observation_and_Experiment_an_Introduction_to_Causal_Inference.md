# Observation and Experiment: An Introduction to Causal Inference

[Book Link](https://www.amazon.com/Observation-Experiment-Introduction-Causal-Inference/dp/0674241630/ref=sr_1_1?crid=UQIIXTVGBIRX&dchild=1&keywords=observation+and+experiment+an+introduction+to+causal+inference&qid=1601735207&sprefix=Observation+and+ex%2Caps%2C157&sr=8-1)

[TOC]

## Unorganized Thoughts

* Quote (page 38): "People often want more than this from a test of a null hypothesis. They desire to know whether the
  hypothesis is true or false, not whether available data constitute strong evidence against the null hypothesis or else
  provide little guidance about its truth. This is a forlorn desire, for it is not hypothesis testing but the world
  itself that refuses to comply."
	* "Can you prove causality with statistics?"
		* Beyond **all doubt**, no; beyond **a reasonable doubt**, absolutely.

* Quote (page 44): "It is an enormous, unforgivable mistake to interpret 'accepting the null hypothesis' as providing
  evidence that the null hypothesis is true. 'Accepting a null hypothesis' means failing to provide much evidence about
  whether it is true or false."

* (page 77): The outlined section makes the point that if an investigator were to say, "this treatment has an effect"
  without looking into whether an observed or unobserved covariate affects the probability of receiving treatment, he
  would be making a mistake.

  To me the question then becomes how can an observational study **ever** overcome this argument? If an extremely
  cautious investigator adjusts for observed covariates $x_1, x_2, x_3$ and additionally makes note of unobserved
  covariates $u_1, u_2, u_3$, what is stopping a critic from saying, "But did you consider unobserved covariate $u_4$?"
  It seems as though one would run into an infinite regress of sorts (I would guess that this is the beauty of
  randomization and there is no way to get around the infinite regress with observational studies).

* Quote (page 105): "The absence of an obvious reason to think that two groups are different falls well short of a
  compelling reason to think they are the same."

* Quote (page 107): "Can an observational study be more than reasonably compelling? Arguably, it has happened once or
  twice, but reasonably compelling studies are rare to begin with."

* Quote (page 134): "The mere existence of consensus is not a useful guide. We should ask, Does a consensus have its
  origins and its ground in a rational and comprehensive appraisal of the evidence? Has the available evidence been open
  to vigorous challeng, and has it met each challenge? If a consensus has these origins, then the existence of consensus
  is of little consequence beyond it's important origins"
  * Objective Reality is the ultimate Truth. The prevalence of an opinion (a "consensus") not based on objective
    reality, no matter how widely held, has absolutely zero bearing on its Truthfulness.

* Quote (page 137): "To say two tests are statistically independent under the null hypothesis $H_0$ of no treatment
  effect is to say that if $H_0$ were true then the result of the first test would provide precisely no information
  about the result of the second...To say that two analyses are vulnerable to different biases is to say that the first
  analysis would be correct if treatment assignment were ignorable in one sense, and that the second analysis would be
  correct if treatment assignment were ignorable in a second sense, *but massive failures of the first sense would not
  bias the second analysis, and massive failures in the second sense would not bias the first analysis.* **This is a
  much stronger property than statistical independence.**"
  * Ignorable treatment assignment occurs when two people with the same values of covariates have the same probability
    of treatment $\pi_i = \pi_j$ - this does not change the fact that these two people $i \text{ and } j$ could both be
    subject to some unobserved bias that alters the conclusion - remember the goal is to think of ways in which a
    hypothesis could be wrong, attempt to prove those hypotheses to be true, and continually fail.

* Quote (page 142): "In the absence of random assignment, there are two possible explanations of a difference in treated
  and control groups; a treatment effect or a bias in the formation of the groups."

## Chapter Insights

### 1

* Randomized group assignment is integral to causal inference because it ensures that the observed covariates $X_i$ of
  patient $i$ have no affect on which group patient $i$ is assigned to, and more importantly, **it ensure that all
  unobserved covariates $U_i$ have no affect on which group patient $i$ is assigned to.**

### 2

* The causal effect of a treatment **can not** be determined for any one individual - if patient $i$ was assigned to the
  treatment group and had a favorable outcome, one can not know if that same patient $i$ would have had that same
  favorable outcome if they were assigned to the control group. This is the only way that one could determine causality
  for patient $i$. Since this is not possible (this is the definition of a counterfactual), causal inference is not
  possible on the individual level.

* The **average** causal effect of a treatment **can** be inferred - randomized group assignment allows an estimate of
  the average treatment effect and an estimate of the average control (no treatment) effect.

### 3

* Uniformity trial - An experiment (often ran in the 1920's and 1930's) where the distinction between treatment and
  control groups was retained, however **both groups received the same treatment (or both groups didn't receive
  treatment).** This allows one to think about one of the fundamental questions of hypothesis testing, "What could we
  expect to happen that is due to chance variation?"
	* Typically used in an agricultural context to determine if fertilizer A was better than fertilizer B, a farm
	  would be randomly divided into many plots and assign a plot to use either fertilizer A or B. **However, all
	  plots were treated the same way (either fertilizer A or B) - giving the investigator an answer to the
	  question, "What can be expected due to random variation?"

* The wording of Fisher's hypothesis of no affect (see Page 349 reasoning check) is very useful in building the intution
  of causal inference in hypothesis testing.

  Fisher's hypothesis of no affects states that each subject would have the same response that was observed whether they
  were in the treatment or control group. Said slightly differently, if a subject received the treatment and had a
  positive outcome, they would have experienced that positive outcome even if they were in the control group.
  Conversely, if a subject that didn't receive treatment (i.e. was in the control group) had a negative outcome, they
  would have experienced that negative outcome even if they had received treatment.

  So, it assumed that nothing would change if the group assignment vector had been different. With this in mind,
  hypothesis testing answers the question, "In how many of the ${n \choose k}$ possible group assignment vectors would
  we have observed results as extreme or more extreme than those that were observed?"

Example:

$$ \begin{align} \text{Observed Group Assignment Vector} & = \left[ T_1, T_2, C_3, T_4, T_5, T_6, C_7, C_8, C_9, C_{ 10
} \right] \\ \text{Observed Response Vector} & = \left[ 1_1, 0_2, 0_3, 1_4, 1_5, 1_6, 0_7, 0_8, 1_9, 0_{ 10 } \right] \\
\end{align} $$

In this scenario, there are 10 subjects (see subscripts), with 5 in the control group and 5 in the treatment group.

$$ {n \choose k} = \frac{ n! }{ (n - k)! \cdot k! } = \frac{ 10! }{ (10 - 5)! \cdot 5! } = \frac{ 10! }{ 5! \cdot 5!} =

\frac{10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot \cancel{ 5 } \cdot \cancel{ 4 } \cdot \cancel{ 3 } \cdot \cancel{2} \cdot
\cancel{1}}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \cdot \cancel{5} \cdot \cancel{ 4 } \cdot \cancel{ 3 } \cdot \cancel{2}
\cdot \cancel{1}} =

\frac{ 30,240 } { 120 } = 252 $$

Which means there are 252 ways to have 5 subjects in the treatment group and 5 subjects in the control group. Since our
Group Assignment Vector is one of those 252, the probability it was chosen is $\frac{1}{252}$, just like all the others.

```R Observed_Response_Vector Group_Assignment_Vector 0 1 Control   4 1 Treatment 1 4(T) ```

The contingency table above shows the relationship between the two variables.  The question now becomes, "In how many of
the 252 possible group assignment vectors would we see a similar result?" More specifically, "What proportion of the 252
possible group assignment vectors would have 4 or more treated subjects with a positive outcome
(`Observed_Response_Vector` = 1)?"

Once again, the wording of Fisher's hypothesis of no effect sets up a direct answer to this question; since the
hypothesis states that the Observed Response Vector would not change, we can computationally create all 252 versions of
the above table and calculate the T statistic and therefore the p value:

```R ##################################### # Everything that could have happened #####################################
Observed_Response_Vector <- c(1,0,0,1,1,1,0,0,1,0) possible_treatment_group_assignment_vectors <- t( combn(10, 5) )

null_distribution_T <- c() for (i in 1:dim(possible_treatment_group_assignment_vectors)[1]) {

	idx <- possible_treatment_group_assignment_vectors[i,] group_assignment_vector <- rep(0, 10)
	group_assignment_vector[idx] <- 1

	T_ <- group_assignment_vector %*% Observed_Response_Vector null_distribution_T <- c(null_distribution_T, T_) }

manual_p_val <- 2 * length( null_distribution_T[null_distribution_T >= 4] ) / length(null_distribution_T)

##################################### # What actually happened #####################################
Observed_Treatment_Group_idx <- possible_treatment_group_assignment_vectors[22,] Observed_Group_Assignment_Vector <-
rep(0, 10) Observed_Group_Assignment_Vector[Observed_Treatment_Group_idx] <- 1

comp_p_val <- fisher.test( Observed_Group_Assignment_Vector, Observed_Response_Vector )[[ 'p.value' ]]

all.equal( manual_p_val, comp_p_val )

> manual_p_val
[1] 0.2063492
```

### 5

* "The central problem in an observational study - **the problem that defines the distinction between a randomized
  experiment and an observational study** - is that treatments are not assigned to subjects at random."

  The **Propensity Score** is at least one of, if not [the central
  tool](https://academic.oup.com/biomet/article/70/1/41/240879?searchresult=1) in attempting to reign in the downstream
  effects of this fact. The propensity score is the conditional probability of treatment given the observed covariates,
  $P(Z = 1 | X)$.  In other words, given a data set, and two covariates (i.e age & sex), the propensity score of 50
  years old males is the average of the group assignment vector for 50 year old males. This can be interpretted as the
  "propensity towards exposure to treatment."

  This score can be used to create matched pairs; where subjects with the same propensity score and observed covariates
  are matched, ensuring that one subject is in the treatment group and one is in the control group. This allows
  investigators to more accurately estimate treatment effects since their estimate can't be skewed by an imbalance in
  one of the observed covariates.

  Example: A financial aptitude test is given at the of each school year to a group of 13-15 year olds. 100 teachers
  teach curriculum A, and 100 teachers teach curriculum B. The study aim is to determine which curriculum leads to
  higher test scores. If an investigator were to ignore propensity score and just compare the two groups, the estimate
  might be misleading; What if the students that were taught curriculum A were mostly from higher income households and
  neighborhoods, where financial literaly is taught at a younger age? What if the students that were taught curriculum B
  study 4 more hours per night than those that were taught curriculum A? These are both examples of covariates (perhaps
  observed, perhaps unobserved) that would bias the estimate. The proper thing to do would be to create matched pairs of
  one curriculum A student and one curriculum B student who are similar in terms of observed covariates and propensity
  scores.

  What is the probability that a student who studies 4 extra hours per night and comes from a low income household was
  taught curriculum A? Find a student who studies the same amount and also comes from a low income household and was
  taught curriculum B. This is one pair. Repeat for the entire data set.

  It is important to note that although matching and using propensity scores balances for observed covariates, **there
  is no basis to assume that unobserved covariates are balanced.**

* Note: The propensity score $\lambda_i$, is **not** the same as the *True* probability of treatment $\pi_i$. To
  reiterate, the propensity score is the **average** probability of treatment given observed covariate(s) $x$. **It is
  created from the data you have, and thus suffers from the same critique that all data sets suffer from; "What isn't
  within the data that is effecting it?"**Two subjects could have the same propensity score because they have the same
  measured covariates, $\lambda_i = \lambda_j$, however their actual probabilities of treatment are different, $\pi_i
  \ne \pi_j$, due to some unmeasured covariate.

### 7

* **Elaborate Theories & The Crossword Puzzle Analogy**: (page 119) "About 20 years ago, when asked in a meeting what
  can be done in observational studies to clarify the step from association to causation, Sir Ronald Fisher replied:
  'Make your theories elaborate'."

  "An elaborate theory makes extensive predictions about what will be observed, so it is less likely to be true that a
  theory that makes fewer predictions, and it is more likely to be contradicted by observed data." (page 124)

  It is important to recognize that structuring a scientific investigation this way is an effort to ensure that the
  theory must "do more work" to prove itself, as opposed to simpler, less elaborate theories which could pass with less
  support of their truth (remember, the goal is not to *prove* a theory, but rather to try and *disprove* it and be
  unable to do so). This leads to the second important aspect of elaborate theories; since the multi-dimensional
  predictions of an elaborate theory can be (must be) checked against observed data, evidence of causal effect in an
  elaborate theory is almost certainly going to be predicated on the conclusions of **many** studies, **not just one.**
  More importantly, "The critical issue is whether the vulnerability that makes one study doubtful is absent from
  another study."

  This brings us to the Crossword Puzzle Analogy. When deciding whether a word is the desired entry into a crossword,
  there are multiple points of contact with what is known; you have the clue given with the puzzle, in addition to the
  other entries that intersect with the one in question, providing evidence that the word you are considering is a most
  likely a "good fit." The same theme is true with elaborate theories and observational studies; much of the evidence
  that an elaborate theory is true is built on the intersection of themes within multiple studies.

  If one study is vulnerable to the claim "unobserved covariate $u_1$ is the reason for the results, not a treatment
  effect," but another study clearly accounts for that unobserved covariate $u_1$ (perhaps it is no longer unobserved
  and is this time explicitly measured and matched for), one must justify continued skeptism of the theory by the claim
  that $u_2$ is now the culprit of a perceived treatment effect. As this continues, a true elaborate theory will
  continually answer claims of bias via additional studies that explicitly control for that bias.

### 9

* (page 171): "A sensitivity analysis asks, How would the results of the calculation, or the conclusion, change if the
  assumptions were changed by a limited amount...How large would the violation of the assumptions have to be to
  materially alter the conlusion?"

  Ignorable treatment assignment, once again, means that two people $i \text{ and } j$ who look the same with respect to
  measured covariates $x_i = x_j$ have the same probability of receiving treatment $\pi_i = \pi_j$. PSM (Propensity
  Score Matching) ensures that in a given pair $P$, there is one treatment and one control, and the subjects are matched
  for a/some covariates, and the others are checked to be within a reasonable range of one another. So, if the Ignorable
  treatment assignment assumption is true, then $\pi_i = \pi_j$, and since there is one treatment subject and one
  control subject, the probability that either is treatment is $\theta = 0.5$.  However, the "if ignorable treatment
  assignment..." statement is a big if.

  A sensitivity analysis **quantifies** the departure from ignorable treatment assignment. Even though we have used PSM
  to match as best we can, what if $\pi_i \ne \pi_j$? Since $\pi_i \ne \pi_j$, then $\theta \ne 0.5$; how far off of 0.5
  must $\theta$ be in order to change the conclusion?

  The table on page 178 shows various measures of this "departure from 0.5".  This is useful against the common critique
  of observational studies; "the treatment effect you are picking up isn't a treatment effect at all, but an unmeasured
  covariate $u_1$ that is changing who receives treatment." Although this is always a valid concern with observational
  studies, if the investigator has performed a sensitivity analysis, this statement is now quantified.

  Example: If an investigator has performed a sensitivity analysis and confirmed that the conclusion of the study is
  insensitive to bias up to a gamma value of 3, $\Gamma = 3$, one can see in the table that $\theta$ can be anywhere in
  the range [0.25, 0.75]. This means that one subject ( in a pair ) may indeed have a higher propensity towards
  treatment, but that probability can be 3 times that of the control $(3 \cdot 0.25 = 0.75)$ **before the conclusion of
  the study would materially change.**

### 11 - Matching Techniques

* Creating the most effective matched pairs one can comes down to a problem of minimizing the total distance between
  pairs, similar to RSS in linear regression or ICV (Intra-Cluster Variance) in Kmeans. Typically, a margin of error is
  set on the propensity score, so two scores must be within a given distance of one another $| \pi_i - \pi_j | \leq k$

* (page 218) "So a simple distance places a caliper on the propensity score; when persons $i$ and $j$ are within the
  caliper on the propensity score, it defines the distance between $i$ and $j$ to be a robust version of the [
  Mahalanobis distance ](https://en.wikipedia.org/wiki/Mahalanobis_distance)"

* As mentioned earlier in the book, matching across all covariates measured is impossible, so tradeoffs must be made.
  Does allowing a marginal increase in the dissimilarity between $x_{i,1}$ and $x_{j,1}$ allow $x_{i,2}$ and $x_{j,2}$
  to be a better match? This must be considered, and the problem context at hand should have a say in how this decision
  is made (if $x_1$ is thought to be an effect modifier, than it should be exactly matched for, while $x_2$ should be
  allowed to vary a little, although still checked, simply by using the propensity score).

* As with all things related to probability, propensity scores work best when you have the Law of Large Number on your
  side; if the N in the study is sufficiently large, using the propensity score alone will likely lead to treatment and
  control groups that are well balanced across many covariates (still check covariate balance table though...)

  In small N studies, **or in studies where certain aspects of patients are sparse across many covariates**, the
  propensity score might not be enough.  Additionally, if these aspects/covariates are important to the study aims, one
  might want to force balance (referred to as "fine balance") between the treatment and control groups.

  **Remember, "You are almost always optimizing, and very rarely maximizing."** This means that in order to match for
  sparse values of one or more covariates, you are probably going to have to let some other covariates and/or the
  propensity score become less balanced than they otherwise would have been.

* **Risk Set Matching:** Fairly often, one would like to investigate the causal effect of a treatment that occurred for
  some subjects, but did not occur for others.

  In order to do this properly, subjects that were treated at timepoint $t$ should be matched with a control, **based on
  the control's covariates at timepoint $t$**. There is the possibility that the control subject in this pair becomes
  treated at a later timepoint $t' \gt t$, and that is okay; assuming the treatment has a positive outcome for
  explanations' sake, it simply changes the hypothetical conclusion from "Treatment had a positive outcome" to "Being
  treated earlier is better than being treated later."

  If the control does not become treated later, than the hypothesis is rather simple:
	* $H_0$: Being treated does not improve outcomes.
	* $H_a$: Being treated improves outcomes.

  Since the treatment and control groups either receive treatment or not, this a a "normal" hypothesis test.

  If the control **does** become treated later, than the hypothesis might be set up as the following:
	* $H_0$: Being treated earlier does not improve outcomes.
	* $H_a$: Being treated earlier improves outcomes.

  In this setting, both the treatment and control receive treatment, **however the defining characteristic is that those
  in the treatment group received treatment earlier than those in the control group.** Since matching occurred at the
  timepoint that the treatment subject received treatment, we are getting at the question, "What would have happened if
  we had waited to treat the subject?"

### 12

* Quote (page 234): "A generic unobserved bias is an unobserved covariate $u$ that promotes **several treatments at the
  same time in a parallel way.**"

  This is where teasing apart the *individual* effect of a treatment is tricky.  How do you know that the outcome you
  are observing is due to treatment A, and not due to treatment B, or the interaction between treatment A and treatment
  B, both of which are *caused* by generic unobserved bias $u$?

  When accounting for this in observational studies, especially when using matching in observational studies, it is
  important to think about what you want to match on.

  The goal of matching is to pair very similar (identical in some ways) subjects (one treatment, at least one control).
  Since observed covariates are the only covariates we have access to, these are our only options to use for matching.
  
  What if matching on observed covariates *amplifies* unobserved generic biases, as opposed to *tempering* them?

  Example: You are conducting a study to determine the effect of prenatal alcohol consumption on long term career
  "success". So, the mechanical investigator goes about his matching algorithm per usual, matching on the following
  covariates; age, education level, parental involvement in parent-teacher confererences....

  The goal is to determine if prenatal alcohol consumption **alone** has a causal effect on long term career success.
  Prenatal alcohol consumption is likely a good indicator of poor parenting. What else does poor parenting this lead to?
  1. Poor care of the child during its formative years?
  2. Lack of involvement in the child's educational development?
  3. Lack of involvement in the child's emotional development?

  Each of these poses a problem to the study. The generic unobserved bias is poor parenting. A mechanical investigator
  might go about his matching algorithm, matching on the parents involvement in parent-teacher conferences, presence at
  the child's sporting events, amount of play time spent with their child, etc. What you end up with are some pairs whose
  parents:
  * **Never** go to parent-teacher confererences, **Never** go to the child's sporting events and **Never** spend any
    play time with their child.

  or...

  * **Always** go to parent-teacher confererences, **always** go to the child's sporting events and **always** spend a
    lot of play time with their child.

  This might (most likely will) bias the study; how do we know that the presence (or lack thereof) of the parents in the
  child's life was the cause of the child's career "success"?

  In order to determine if prenatal alcohol consumption **alone** has an effect on long term career success, ideally we
  would be able to decouple poor parenting from prenatal alcohol consumption. One way to do this is **intentionally pair
  subjects with different values of observed covariate $x$.** *The goal of this process is to match (as best as possible)
  on the value of the unobserved generic bias $u$.*

  So, continuing with the example, one might intentionally create a pair $i,j$ where:
  * Subject $i$'s parents usually show up to parent-teacher confererences and subject $j$'s parents usually do not show
    up.
  * Subject $i$'s parents usually are not at the child's sporting events and subject $j$'s parents usually are.
  * etc.

  A pair like the above is a pair where both subject's parents are likely to have a middle "value" of the unobserved
  generic bias $u$. That is, by creating a pair that isn't a good match on values of observed covariates, we have a
  created a pair that is a good match on the value of the more important unobserved covariate.

### 13 - Instruments

* Quote (page 258): "An instrument is a random push towards receiving one treatment rather than another, a push that is
  without consequences for outcomes unless it succeeds in changing the treatment received."

* Quote (page 267): "The exclusion restriction means that the average effect of encouragement, $\bar{\delta}$, is an
  average of many zeros for people who would not heed encouragement and some possibly nonzero $\delta_i$'s for compliers
  who heed encouragement."

* Exlusion Restriction: In a "normal" randomized experiment, the subjects that are assigned to the treatment group all
  receive the treatment. Therefore, the average effect, $\bar{\delta}$, is averaged across the number of people in the
  treatment group.

  Since instruments are about *some* people being pushed towards one treatment in favor of another, the average effect,
  $\bar{\delta}$, **is only averaged over those who actually received the treatment.**


![](images/Observation_and_Experiment_an_Introduction_to_Causal_Inference/exclusion_restriction.png)


## Reasoning Checks

### Page 36: "There are 70 ways to pick $m = 4$ patients for treatment from $I = 8$."

**The Binomial Connection to Randomized Group Assignment**

Since order doesn't matter, the formula for combinations should be used: (the group assignment vector
[1,1,1,1,0,0,**0**,0] isn't materially different from the group assignment vector [1,1,1,1,0,0,0,**0**]; the $7^{th}$
patient is still in the control group (0) and the $8^{th}$ is still in the control group; moving the **bold 0** doesn't
change that fact), the formula for combinations should be used:

$$
{n \choose k} = \frac{ n! }{ (n - k)! \cdot k! } = \frac{ 8! }{ (8 - 4)!  \cdot 4! } = \frac{ 8! }{ 4! \cdot 4!} =

\frac{8 \cdot 7 \cdot 6 \cdot 5 \cdot \cancel{ 4 } \cdot \cancel{ 3 } \cdot \cancel{2} \cdot \cancel{1}}{4 \cdot 3 \cdot
2 \cdot 1 \cdot \cancel{ 4 } \cdot \cancel{ 3 } \cdot \cancel{2} \cdot \cancel{1}} =

\frac{ 1680 } { 24 } = 70
$$

This gives us the number of unique ways that 8 items can be arranged when order doesn't matter. Referencing the context
of the book, this also gives us the "Treatment Indicators" section of table 3.2; this can be thought of as the "Binary
Manifestation of Possible Group Assignment Vectors". The subscript of each number below indicates the patient ID, while
the number 1 or 0 indicates if patient $i$ was in the treatment group (1) or the control group (0).

$$
\left[ 1_1,1_2,1_3,1_4,0_5,0_6,0_7,0_8 \right] \\
\left[ 1_1,1_2,1_3,0_4,1_5,0_6,0_7,0_8 \right] \\
\left[1_1,1_2,1_3,0_4,0_5,1_6,0_7,0_8 \right] \\
\vdots \\
\left[ 0_1,0_2,0_3,1_4,0_5,1_6,1_7,1_8 \right] \\
\left[0_1,0_2,0_3,0_4,1_5,1_6,1_7,1_8 \right]
$$

Re-written to illustrate the the probabilistic underpinnings of the "Binary Manifestation of Possible Group Assignment
Vectors,", we get the "Probabilistic Representation of Possible Group Assignment Vectors." (Note that since there is an
equal probability of being assigned a 1 or 0, $P = 1 - P = 0.5$. In order to clearly show "which 0.5" I'm referring to,
a **bold** $\pmb{0.5_i}$ will mean that patient $i$ ended up in the control group (0), whereas a normal typeface $0.5_i$
will indicate that patient $i$ ended up in the treatment group (1))

$$
\left[ 0.5_1,0.5_2,.0.5_3,0.5_4,\pmb{ 0.5_5 },\pmb{ 0.5_6 },\pmb{ 0.5_7 },\pmb{ 0.5_8 } \right] \\
\left[0.5_1,0.5_2,.0.5_3,\pmb{ 0.5_4 },0.5_5,\pmb{ 0.5_6 },\pmb{ 0.5_7 },\pmb{ 0.5_8 } \right] \\
\left[0.5_1,0.5_2,.0.5_3,\pmb{ 0.5_4 },\pmb{ 0.5_5 },0.5_6,\pmb{ 0.5_7 },\pmb{ 0.5_8 } \right] \\
\vdots \\
\left[ \pmb{ 0.5_1},\pmb{ 0.5_2 },.\pmb{ 0.5_3 },0.5_4,\pmb{ 0.5_5 },0.5_6,0.5_7,0.5_8 \right] \\
\left[ \pmb{ 0.5_1 },\pmb{ 0.5_2},.\pmb{ 0.5_3 },\pmb{ 0.5_4 },0.5_5,0.5_6,0.5_7,0.5_8 \right]
$$

The above is the "expanded" version of the Binomial PMF (shown below) when $n = 8, k = 4, P = 0.5$. Reading this within
the context of the book, this says "There are 70 unique ways to arrange 4 $(0.5)$ terms and 4 $\pmb{0.5}$ terms."

$$
(70) ( 0.5 )^4 ( \pmb{ 0.5 } )^4
$$

Reading the above within the context of the Binomial PMF, this says, "The probability that one observes $k = 4$
successes out of $n = 8$ independent trials is equal to 0.27"

$$
\begin{align}
P(X = k) & = {n \choose k} ( P )^k (1 - P)^{n -k} \\
& = (70) ( 0.5 )^4 ( \pmb{ 0.5 } )^4 \\
& = (70) ( 0.5 )^8 \\
P(X =4) & = 0.2734
\end{align}
$$

### Page 45 "Fisher's Exact Test; the 'Reasoned Basis for Inference'"

* "The word 'exact' means that the distribution in Table 3.5 is exactly the distribution of the test statistic $T$ in a
  completely randomized experiment when Fisher's null hypothesis is true. That is, Table 3.5 is exactly the null
  distribution of $T$, not an approximation to its null distribution."
	* Rosenbaum hints at the fact that distribution approximations are usually okay and are widely used in
	  statistics. However, if one can avoid them, that is one assumption less to worry about being wrong.

### Page 60 "So volunteering and self-selection in the randomized trial did nothing to create bias in the comparison of treated and control groups."

* This sentence touches again on a main theme of the book; random group assignment **ensures** that there isn't some
  unobserved group assignment algorithm, while this can never be gauranteed with observational studies. More
  specifically, ensuring that random group assignment is performed **after** anyone that doesn't want to participate in
  the study drops out is what gaurantees the above sentence.

### Page 84: "The problem [causation being inferred due to combining strata with different probabilities of receiving treatment] recurs because two randomized experiments with different probabilities $\pi_i$ were merged"

* Does this mean that is is *always* valid to merge strata that had the same probability of treatment $\pi_i = \pi_j$?
  I'm guessing that the answer to that question depends on whether the data was generated from a randomized experiment
  vs. observed in the world (observational data)...

### Page 268: " If $\bar{\eta} \ne 0$ but $\bar{\eta}$ is near zero, then the parameter $\frac{\bar{\delta}}{\bar{ \eta }}$ is well defined, but estimates of $\frac{\bar{\delta}}{\bar{ \eta }}$ can be very unstable."

* Presumably this has nothing to do with the concept of instruments or effect ratios, but is simply a low $n$ problem.
  Since $\frac{\bar{\delta}}{\bar{ \eta }}$ is the "average effect of encouragement on compliers" $\bar{\eta}$ being
  close to 0 means you have very few compliers (people who would change their behavior if encouraged but otherwise would
  not change their behavior).

  So the instability of the estimate is likely more due to the fact that the estimate is based on a small sample of
  compliers.

### Page 271: "...Do high-level NICU's save more lives?"

* This is a question that is a clear example of the need to ensure that one is comparing two things that are indeed
  comparable. Right off the bat, I could see how an un-inquisitive investigator, if he did not use matching techniques,
  could come up with an answer of "No, high level NICU's do not save more lives.  In fact, it appears that high level
  NICU's 'lose' more lives."
	* I think it is safe to assume that, if a mother and father know they are going to have a baby born premature
	  (perhaps with more complications than a baby that is born less premature), they might go out of their way to
	  seek out a NICU with a higher rating. This could then lead to the average acuity of babies in highly rated
	  NICU's being well above the average acuity of babies in lower rated NICU's.  Matching for acuity level (weeks
	  premature, genetic complications, etc) would be the minimum needed to ensure comparability.

### Page 272: "...The hope is that, having matched for many covariates, there is nothing special about mothers who live near or far from a hospital with a high-level NICU."

* Since the mothers in this study were matched for socioeconomic status, one shouldn't run into the problem of
  "Wealthier mothers might have to superior hospitals" - very important to match for this covariate.

There are "known known's" ($x_i$), there are "known unknown's" ($u_i$) and finally the "Unknown unknown's" (covariates
that you are completely unaware of that might bias the outcome)

### Page 349: Fisher's null hypothesis of no difference in treatment effects

"This null hypothesis, $H_0$, asserts that each person would have the same response under treatment as under control,
$r_{Ti} - r_{Ci} = 0$ for $i = 1, \cdots, I$, or equivalently, $\delta_i = 0$ for $i = 1, \cdots , I$.  Often
abbreviated as Fisher's hypothesis of no effect."


