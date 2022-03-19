This book was read in conjunction with the [ MIT OCW 18.06SC Lectures ](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
and therefore the notes will be from both the book and the lectures.

# Introduction to Linear Algebra, 5th Ed.

[Book Link](https://www.amazon.com/Introduction-Linear-Algebra-Gilbert-Strang/dp/0980232775/ref=sr_1_2?dchild=1&keywords=Gilbert+strang&qid=1610361218&sr=8-2)

[TOC]

## Unorganized Thoughts

### Statistical Learning Tie-In: Structured Data as a "Snapshot" of a Population $f(x)$

* Structured data is typically represented as an $n \text{ x } p$ matrix, where $n$ is interpreted as the
  rows/observations, and $p$ is interpreted as the measured attributes/variables of those observations.
* An image is also represented as an $n \text{ x } p$ matrix, where $n$ is interpreted as the height of the image and
  $p$ is interpreted as the width of the image.
* 

## Chapter Insights

### 2

$$
\begin{align}
\text{if } \mathbf{w} & = a  \mathbf{u} + b\mathbf{v} \text{ (linear transformation of vectors) }\\
\text{then } \mathit{A}\mathbf{w} & = a \mathit{A}\mathbf{u} + b \mathit{A}\mathbf{v} \text{ (linear transformation of matrices) }
\end{align}
$$

#### Elimination Algorithm

##### Abstract

(This all assumes a nonsingular matrix)

An $n \text{ x } n$ matrix $A$ will have $n$ total 'elimination matrices':

$$
\begin{align}
E^n E^{n-1} E^{n-2} \cdots E^3 E^2 E^1 A\bold{x} & = E^n E^{n-1} E^{n-2} \cdots E^3 E^2 E^1 \bold{b} \\
U\bold{x} & = \bold{c}
\end{align}
$$

In order to make referencing each stage in elimination easier, let $T^n$ be the transformed matrix that results from
multiplying $A$ by the first $n$ elimination matrices:

$$
\begin{align}
T^0 & = A\bold{x} \\
T^1 & = E^1 A\bold{x} \\
T^2 & = E^2 E^1 A\bold{x} \\
T^3 & = E^3 E^2 E^1 A\bold{x} \\
T^n & = E^n E^{n-1} E^{n-2} \cdots E^3 E^2 E^1 A\bold{x}\\
\end{align}
$$

To construct the $n^{th}$ elimination matrix, follow the below algorithm:

1. Let $E^n$ be the elimination matrix used to create 0's below the $n^{th}$ pivot.
2. The diagonal will be all 1's, all entries above the diagonal will all be 0, and all entries below the diagonal that
   **are not in the $n^{th}$ column** will all be 0.
3. All entries of $E^n$ in the $n^{th}$ column (below the 1 that is in the diagonal) will be:

$$
E^n_{i,n} = -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} }
$$

For example:

$$
\begin{align}
    E^1 & =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 1 & 0 & 0 & \cdots & 0 \\
    -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 0 & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 0 & 0 & 0 & \cdots & 1 \\
    \end{bmatrix}

    E^2 && =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 & 0 & \cdots & 0 \\
    0 & -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 0 & 0 & \cdots & 1 \\
    \end{bmatrix}

    E^3 && =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 & 0 & \cdots & 0 \\
    0 & 0 & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & -\frac{ T^{ n-1 }_{i,n} }{ T^{ n-1 }_{n,n} } & 0 & \cdots & 1 \\
    \end{bmatrix}

    \\

    & =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    -\frac{ T^{ 0 }_{2,1} }{ T^{ 0 }_{1,1} } & 1 & 0 & 0 & \cdots & 0 \\
    -\frac{ T^{ 0 }_{3,1} }{ T^{ 0 }_{1,1} } & 0 & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    -\frac{ T^{ 0 }_{n,1} }{ T^{ 0 }_{1,1} } & 0 & 0 & 0 & \cdots & 1 \\
    \end{bmatrix}

    && =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 & 0 & \cdots & 0 \\
    0 & -\frac{ T^{ 1 }_{3,2} }{ T^{ 1 }_{2,2} } & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & -\frac{ T^{ 1 }_{n,2} }{ T^{ 1 }_{2,2} } & 0 & 0 & \cdots & 1 \\
    \end{bmatrix}

    && =
    \begin{bmatrix}
    1 & 0 & 0 & 0 & \cdots & 0 \\
    0 & 1 & 0 & 0 & \cdots & 0 \\
    0 & 0 & 1 & 0 & \cdots & 0 \\
    \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & -\frac{ T^{ 2 }_{n,3} }{ T^{ 2 }_{3,3} } & 0 & \cdots & 1 \\
    \end{bmatrix}

\end{align}
$$

##### Code 

```python
import unittest
import numpy as np

class EliminationSolver(object):
    def __init__(self, A, b):
        self.A = A
        self.b = b
        self.Es = np.array( [np.identity(self.A.shape[0]) for _ in range( self.A.shape[0]-1 )] )
        self.bs = [self.b]
        self.Ts = [self.A]
    def solve(self, T, elim_step):
        for i in range(elim_step, T.shape[0]-1):
            if T[i+1,elim_step] != 0:
                self.Es[elim_step][i+1,elim_step] = -(T[i+1,elim_step] / T[elim_step,elim_step])
        self.Ts.append(self.Es[elim_step].dot(self.Ts[-1]))
        self.bs.append(self.Es[elim_step].dot(self.bs[-1]))
    def solve_iter(self):
        total_elim_steps = self.A.shape[0]-1
        for elim_step in range(total_elim_steps):
            self.solve(T=self.Ts[-1], elim_step=elim_step)
        final = np.array( self.Ts[-1] )
        # NOTE: doesn't really count as 'from scratch' if you're using numpy's
        # inverse function, does it now Marshall...
        final_inv = np.linalg.inv(final)
        self.solution = final_inv.dot(self.bs[-1])

class TestCustomElimination(unittest.TestCase):
    def test_1(self):
        A = np.array([
            [2,1,0,0],
            [1,2,1,0],
            [0,1,2,1],
            [0,0,1,2]
            ])
        b = np.array([0,0,0,5]).reshape(-1,1)
        np_test_result = np.linalg.solve(A, b)

        solver = EliminationSolver(A=A, b=b)
        solver.solve_iter()
        print(solver.solution)

        self.assertTrue(np.allclose( np_test_result, solver.solution, equal_nan=True ))
    def test_2(self):
        A = np.array([
            [2,-1,0,0],
            [-1,2,-1,0],
            [0,-1,2,-1],
            [0,0,-1,2]
            ])
        b = np.array([0,0,0,5]).reshape(-1,1)
        np_test_result = np.linalg.solve(A, b)

        solver = EliminationSolver(A=A, b=b)
        solver.solve_iter()
        print(solver.solution)

        self.assertTrue(np.allclose( np_test_result, solver.solution, equal_nan=True ))

if __name__ == '__main__':
    unittest.main()
```

##### Example: 3x3 Matrix

Starting with the standard linear equation (below)...

$$
\begin{align}
    A\bold{x} & = \bold{b} && \text{standard linear equation} \\
    \begin{bmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i \\
    \end{bmatrix}
    & =
    \begin{bmatrix}
    x \\
    y \\
    z \\
    \end{bmatrix} && \text{Note that the } \bold{x} \text{ is implicit in } A \text{ from this point forward}
\end{align}
$$

...the goal is to find a series of matrices that transform $A\bold{x}$ into an upper triangular matrix $U$ such that back
substitution can be used:

$$
    \begin{bmatrix}
    a & b & c \\
    0 & j & k \\
    0 & 0 & l \\
    \end{bmatrix}
    =
    \begin{bmatrix}
    m \\
    n \\
    o \\
    \end{bmatrix}
$$

###### Step 1

Use the first equation to create a matrix that creates all 0's below the first pivot (i.e. eliminates all numbers below
the first pivot). This first 'elimination matrix' will have the following general form:

$$
    E^1 =
    \begin{bmatrix}
    1 & 0 & 0 \\
    -\frac{d}{a} & 1 & 0 \\
    -\frac{g}{a} & 0 & 1 \\
    \end{bmatrix}
$$

Multiplying both sides of $A\bold{x} = \bold{b}$ by this first 'elimination matrix' results in:

$$
\begin{align}
    E^1 \left( A\bold{x} \right)
    & =
    E^1 \left( \bold{b} \right)

    \\

    \begin{bmatrix}
    1 & 0 & 0 \\
    -\frac{d}{a} & 1 & 0 \\
    -\frac{g}{a} & 0 & 1 \\
    \end{bmatrix}
    \left(
    \begin{bmatrix}
    a & b & c \\
    d & e & f \\
    g & h & i \\
    \end{bmatrix}
    \right)
    & =
    \begin{bmatrix}
    1 & 0 & 0 \\
    -\frac{d}{a} & 1 & 0 \\
    -\frac{g}{a} & 0 & 1 \\
    \end{bmatrix}
    \left(
    \begin{bmatrix}
    x \\
    y \\
    z \\
    \end{bmatrix}
    \right)

    \\

    \begin{bmatrix}
    a & b & c \\
    \cancel{ a }\left( -\frac{d}{\cancel{ a }} \right)+d & b\left( -\frac{d}{a} \right)+e & c\left( -\frac{d}{a} \right)+f \\
    \cancel{ a }\left( -\frac{g}{\cancel{ a }} \right)+g & b\left( -\frac{g}{a} \right)+h & c\left( -\frac{g}{a} \right)+i \\
    \end{bmatrix}
    & =
    \begin{bmatrix}
    x \\
    x \left( -\frac{d}{a} \right)+y \\
    x\left( -\frac{g}{a} \right)+z \\
    \end{bmatrix}

    \\

    \begin{bmatrix}
    a & b & c \\
    0 & b\left( -\frac{d}{a} \right)+e & c\left( -\frac{d}{a} \right)+f \\
    0 & b\left( -\frac{g}{a} \right)+h & c\left( -\frac{g}{a} \right)+i \\
    \end{bmatrix}
    & =
    \begin{bmatrix}
    x \\
    x \left( -\frac{d}{a} \right)+y \\
    x\left( -\frac{g}{a} \right)+z \\
    \end{bmatrix}
\end{align}
$$

###### Step 2

Use the second equation of the resulting matrix of step 1 to create all 0's below the second pivot (i.e. eliminates all
numbers below the second pivot - which in the 3x3 case is only 1). This second 'elimination matrix' will have the
following general form:

$$
    E^2 =
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & \left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right) & 1 \\
    \end{bmatrix}
$$

Taking the result from step 1, and multiplying both sides by $E^2$, we get:

$$
\begin{align}

    E_2 \left( E_1 A \bold{x} \right)
    & =
    E_2 \left( E_1 \bold{b} \right)

    \\

    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & \left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right) & 1 \\
    \end{bmatrix}
    \left(
    \begin{bmatrix}
    a & b & c \\
    0 & b\left( -\frac{d}{a} \right)+e & c\left( -\frac{d}{a} \right)+f \\
    0 & b\left( -\frac{g}{a} \right)+h & c\left( -\frac{g}{a} \right)+i \\
    \end{bmatrix}
    \right)
    & =
    \begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & \left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right) & 1 \\
    \end{bmatrix}
    \left(
    \begin{bmatrix}
    x \\
    x \left( -\frac{d}{a} \right)+y \\
    x\left( -\frac{g}{a} \right)+z \\
    \end{bmatrix}
    \right)

    \\

    \begin{bmatrix}
    a & b & c \\
    0 & b\left( -\frac{d}{a} \right)+e & c\left( -\frac{d}{a} \right)+f \\
    0 & \cancel{ \left( b\left( -\frac{d}{a} \right)+e \right) }\left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ \cancel{ b\left( -\frac{d}{a} \right)+e } } \right)+\left( b\left( -\frac{g}{a} \right)+h \right) & \left( c\left( -\frac{d}{a} \right)+f \right)\left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right)+\left( c\left( -\frac{g}{a} \right)+i \right) \\
    \end{bmatrix}
    & =
    \begin{bmatrix}
    x \\
    x \left( -\frac{d}{a} \right)+y \\
    \left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right) \left( x \left( -\frac{d}{a} \right)+y \right) + \left( x\left( -\frac{g}{a} \right)+z \right) \\
    \end{bmatrix}

    \\

    \begin{bmatrix}
    a & b & c \\
    0 & b\left( -\frac{d}{a} \right)+e & c\left( -\frac{d}{a} \right)+f \\
    0 & 0 & \left( c\left( -\frac{d}{a} \right)+f \right)\left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right)+\left( c\left( -\frac{g}{a} \right)+i \right) \\
    \end{bmatrix}
    & =
    \begin{bmatrix}
    x \\
    x \left( -\frac{d}{a} \right)+y \\
    \left(- \frac{ b\left( -\frac{g}{a} \right)+h }{ b\left( -\frac{d}{a} \right)+e } \right) \left( x \left( -\frac{d}{a} \right)+y \right) + \left( x\left( -\frac{g}{a} \right)+z \right) \\
    \end{bmatrix}

\end{align}
$$


### 3

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

