# Introduction to Linear Algebra, 5th Ed.

[Book Link](https://www.amazon.com/Introduction-Linear-Algebra-Gilbert-Strang/dp/0980232775/ref=sr_1_2?dchild=1&keywords=Gilbert+strang&qid=1610361218&sr=8-2)

[TOC]

## Unorganized Thoughts

## Chapter Insights

### 2

$$
\begin{align}
\text{if } \mathbf{w} & = a  \mathbf{u} + b\mathbf{v} \text{ (linear transformation of vectors) }\\
\text{then } \mathit{A}\mathbf{w} & = a \mathit{A}\mathbf{u} + b \mathit{A}\mathbf{v} \text{ (linear transformation of matrices) }
\end{align}
$$

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

#### 32 (Page 44)

Prompt:
"Suppose $\mathbf{u}$ and $\mathbf{v}$ are the first two columns in a 3x3 matrix $\mathit{A}$. Which third columns
$\mathbf{w}$ would make this matrix $\mathit{A}$ singular? Describe a typical column picture of $A\mathbf{x} = b$ in
that singular case, and a typical row picture (for a random $\mathit{b}$).

Answer:
* Singular = non-invertible = some columns are linearly dependent on some others.

Formally, $\mathbf{w} = a  \mathbf{u} + b \mathbf{v}$ describes all columns $\mathbf{w}$ that would make the matrix
$\mathit{A}$ singular.

**Column Picture**
$\mathbf{u} \text{ and } \mathbf{v}$ define a plane in $\mathbb{R}^3$; $\mathbf{w}$ lies in that plane and thus the
three vectors do not span all of $\mathbb{R}^3$. **If $\mathbf{b}$ lies in that plane, there are infinite solutions. If
$\mathbf{b}$ does not lie in that plane, there are no solutions.** So, "how the picture looks" depends on $\mathbf{b}$
(check out figure 1.6 in [Linear Algebra and Its Applications, 4th Ed.](https://www.amazon.com/Linear-Algebra-Its-Applications-4th/dp/0030105676/ref=sr_1_7?dchild=1&keywords=gilbert+strang&qid=1614860145&s=books&sr=1-7))

**Row Picture**
How the system "looks" once again depends on $\mathbf{b}$; there are two abstract possibilities:
1. **Infinite solutions** - if two planes (aka equations) in $\mathbb{R}^3$ intersect in a line, and the third plane
   *intersects both the other planes in the same line*, there are infinite solutions (the line itself).
2. **No solution** - if two planes (aka equations) in $\mathbb{R}^3$ intersect in a line, and the third plane intersects
   one or both of the other two planes *such that the the lines defined by the various intersections are parallel*, there
   is no solution.

#### 34 (Page 45)

Knowing that...

$$
\mathit{A}\mathbf{x} = \mathbf{b}
$$

...but being given the definitions of $\mathit{A}$ and $\mathbf{b}$ and
asked to solve for $\mathbf{x}$ (as opposed to being given $\mathit{A}$ and $\mathbf{x}$ and being asked to solve for
$\mathbf{b}$ - the "normal way of doing things"), I can use the below two equalities:

$$
\begin{align}
\text{Equality }1:~& \mathit{A}\mathit{A}^{ -1 } = \mathit{I} = \mathit{A}^{ -1 }\mathit{A} \\
\text{Equality }2:~& \mathit{I}\mathbf{x} = \mathbf{x}
\end{align}
$$

...and "get back" to the "normal way of doing things":

$$
\begin{align}
\mathit{A}\mathbf{x} & = \mathbf{b} && \text{ start } \\
\mathit{A}^{ -1 }\mathit{A}\mathbf{x} & = \mathit{A}^{ -1 }\mathbf{b} &&\text{ multiply by }\mathit{A}^{ -1 } \\
\mathit{I}\mathbf{x} & = \mathit{A}^{ -1 }\mathbf{b} && \text{ substituting Equality } 1 \text{ in left hand side } \\ 
\mathbf{x} & = \mathit{A}^{ -1 }\mathbf{b} && \text{ using Equality } 2 \text{ on left hand side } \\ 
\mathit{A}^{ -1 }\mathbf{b} & = \mathbf{x} && \text{ flipping things around for ease of readability } \\ 
\end{align}
$$

```python
import numpy as np

A = np.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
print(A)
# [[ 2 -1  0  0]
#  [-1  2 -1  0]
#  [ 0 -1  2 -1]
#  [ 0  0 -1  2]]
b = np.array([1,2,3,4])
A_inv = np.linalg.inv(A)
x = A_inv.dot(b)
print(x)
# [4. 7. 8. 6.]


```

#### 35 (Page 45)

Since each row and column in $\mathit{S}$ have the same 9 numbers (1 - 9), if $\mathbf{x} = (1, 1, 1, ..., 1)$, then:

$$
\mathit{S}\mathbf{x} = 
			    \begin{bmatrix}
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    45 \\
			    \end{bmatrix}
$$

```python
out = sum( [i for i in range(1, 10)] )
print(out)
# 45
```

**Which row exchanges will produce another Sodoku matrix?**

No matter how the rows are permuted, the columns will all still be valid; rearranging the order of the number 1 - 9
doesn't change the fact that all those number will still be present in the each column. So the columns will take care of
themselves.

Since each 3x3 grid must also contain the numbers 1 - 9, any row permutations must keep the same group of the rows
together. Therefore, for each group of 3 rows (3 groups total), there are $3! = 3 \cdot 2 \cdot 1 = 6$ different
permutations *of those three rows*.

*Leaf level*
Thinking about one permutation *of the first block* of 3 rows, one permutation *of the second block* of 3 rows, there
are 6 permutations *of the third block* of 3 rows.

$$
1 \cdot 1 \cdot 6 = 6 \\
$$

*Twig level*
Expanding to think about one permutation *of the first block* of 3 rows, **all** 6 permutations *of the second block* of
3 rows, each of which has 6 permutations of the third block of three rows. There are 36 valid permutations.

$$
1 \cdot 2 \cdot 6 = 6 \\
1 \cdot 3 \cdot 6 = 6 \\
\vdots \\
1 \cdot 6 \cdot 6 = 36 \\
$$

*Branch level*
Expanding again to think about **all** 6 permutations *of the first block* of 3 rows, each of which has 36 permutations
of the second and third blocks of three rows. There are 216 valid permutations.

$$
\begin{align}
\mathbf{ 1 } \cdot 2 \cdot 6 = & 6 \\
\mathbf{ 1 } \cdot 3 \cdot 6 = & 6 \\
\vdots \\
\mathbf{ 1 } \cdot 6 \cdot 6 = & \text{ first } 36 \\
\\
\mathbf{ 2 } \cdot 2 \cdot 6 = & 6 \\
\mathbf{ 2 } \cdot 3 \cdot 6 = & 6 \\
\vdots \\
\mathbf{ 2 } \cdot 6 \cdot 6 = & \text{ another } 36 \\
\\
\mathbf{ 3 } \cdot 2 \cdot 6 = & 6 \\
\mathbf{ 3 } \cdot 3 \cdot 6 = & 6 \\
\vdots \\
\mathbf{ 3 } \cdot 6 \cdot 6 = & \text{ another } 36 \\
\vdots \\
\vdots \\
\mathbf{ 6 } \cdot 2 \cdot 6 = & 6 \\
\mathbf{ 6 } \cdot 3 \cdot 6 = & 6 \\
\vdots \\
\mathbf{ 6 } \cdot 6 \cdot 6 = & \text{ another } 36 \\
\vdots \\
6 \cdot 6 \cdot 6 = & 216 \text{ permutations of rows if the blocks of 3 remain unchanged } \\
\end{align}
$$

*Root level*
Expanding for the last time: thinking about **all** 6 permutations of the *3 blocks of 3 rows*, each of which has 216
permutations of all 9 rows. **There are 1296 valid permutations of the rows of a Sodoku matrix.**

$$
\begin{align}
& \left[\text{block permutations}, 1^{st}\text{ block row permutations}, 2^{nd}\text{ block row permutations}, 3^{rd}\text{ block row permutations} \right] \\
& \left[6, 6, 6, 6 \right] \\
& 6^4 = 1296 \\
\end{align}
$$
