# Introduction to Linear Algebra, 5th Ed.

[Book Link](https://www.amazon.com/Introduction-Linear-Algebra-Gilbert-Strang/dp/0980232775/ref=sr_1_2?dchild=1&keywords=Gilbert+strang&qid=1610361218&sr=8-2)

[TOC]

## Unorganized Thoughts

## Chapter Insights

## Reasoning Checks

* $n$ unkown variables in $m$ equations $=$ A solution space that fills $\mathbb{R}^{n-m}$

## Select Problems

There is an error in the text as it is written. Below is a description of the error and how it should be changed.

### Problem Set 1.2

#### 34 (Page 21)

**Current Text**

Using `v = randn(3, 1)` in MATLAB, create a random unit vector $u = \frac{v}{||v||}$. Using `V = randn(3, 30)` create 30
more random unit vectors $U_j$. What is the average size of the dot products $|u \cdot U_j|$? In calculus, the average
is $\int_0^\pi |cos \theta| \frac{d\theta}{\pi} = \frac{2}{\pi}$.

**Suggested Text**

* Changes: the 3 is changed to a 2 in both calls to `randn()`.

Using `v = randn(2 1)` in MATLAB, create a random unit vector $u = \frac{v}{||v||}$. Using `V = randn(2, 30)` create 30
more random unit vectors $U_j$. What is the average size of the dot products $|u \cdot U_j|$? In calculus, the average
is $\int_0^\pi |cos \theta| \frac{d\theta}{\pi} = \frac{2}{\pi}$.

```python
from plotnine import ggplot, aes, geom_histogram, geom_vline, facet_wrap
import pandas as pd
import numpy as np
import numpy.linalg as la

def sample_unit_circle(R_n=2, n=30, verbose_sanity_check=False):
    # create random unit vector
    v = np.random.randn(R_n, 1)
    u = v / la.norm(v)
    # create matrix of unit vectors
    V = np.random.randn(R_n, n)
    vector_lengths = np.sqrt( ( V * V ).sum(axis = 0) )
    U = V / vector_lengths
    # sanity check - should be 30 unit vectors
    if verbose_sanity_check:
        print(f"# Vectors = { len( ( U * U ).sum(axis = 0) ) }")
        print(f"vector lengths = { ( U * U ).sum(axis = 0) }")
    # get all dot products
    return np.absolute( U.transpose().dot(u) ).mean()



samples = {30: [], 50: [], 100: [], 200: []}
repeats = 500
for i in range(repeats):
    for k in samples.keys():
        samples[k].append(sample_unit_circle(n = k))


df = pd.melt( pd.DataFrame(samples) )
df.columns = ['Sample_N', 'Dot_Product_Mean']
(ggplot(df, aes(x = 'Dot_Product_Mean'))
    + geom_histogram(bins = 100)
    + facet_wrap('Sample_N', nrow = 1)
    + geom_vline(xintercept = 2/np.pi, color = 'blue'))
```

### Problem Set 2.1

#### 22 (Page 43)

```python
import numpy as np

A = np.array([[1,2],[3,4]])
x = np.array([5, -2])
b = np.array([1, 7])

A.dot(x) == b
```

#### 29 & 30 (Page 44)

When the markov matrix A...

$$
A = 
    \begin{bmatrix}
    0.8 & 0.3 \\
    0.2 & 0.7 \\
    \end{bmatrix}
$$

...is multiplied by either $u_{0}$ or $v_{0}$...

$$
\begin{align}
u_{0} & = 
    \begin{bmatrix}
    1 \\
    0 \\
    \end{bmatrix}
\\
v_{0} & = 
    \begin{bmatrix}
    0 \\
    1 \\
    \end{bmatrix}
\end{align}
$$

...and the result of the multiplication is itself multiplied by $A$ repeatedly, both $u_{0}$ or $v_{0}$ approach the
steady state vector...

$$
s = 
    \begin{bmatrix}
    0.6 \\
    0.4 \\
    \end{bmatrix}
$$

```python
import numpy as np

# 29
A = np.array([[0.8, 0.3],[0.2, 0.7]])
u_current = np.array([ [1],[0] ])
for i in range(10):
    print(u_current)
    print(u_current.sum())
    u_current = A.dot(u_current)


# 30
v_current = np.array([ [0],[1] ])
for i in range(10):
    print(v_current)
    print(v_current.sum())
    v_current = A.dot(v_current)


steady_state = np.array([ [0.6],[0.4] ])
for i in range(10):
    print(steady_state)
    print(steady_state.sum())
    steady_state = A.dot(steady_state)


```
