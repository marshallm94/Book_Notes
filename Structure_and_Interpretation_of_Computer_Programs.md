# Structure and Interpretation of Computer Programs 

[Book Link](https://mitpress.mit.edu/sites/default/files/sicp/index.html)

[TOC]

## Unorganized Thoughts

* (Spurred by my (moderately hilarious) inability to complete problem 1.3 for ~1 hour during a plane ride, which is due
  to prefix notation being rather foreign) It is interesting ( to me ) to consider that almost no individual would could
  answer the question, "Is prefix notation superior to 'standard' mathematical notation?" without the confounding
  variable of 'experience/familiarity' coming into play. Is standard mathematical notation actually superior to prefix
  notation, or does every individual *encounter* prefix notation after N years of familiarity with 'standard' notation,
  and therefore it feels so foreign that they (including me) call it 'foreign' and dismiss it.

  I wonder how this affects the evolution of programming languages? Is one of the reasons Scheme/Lisp is not as popular
  as Python for example due to the fact that prefix notation is 'too foreign' for any potential programmer, who at the
  time they are writing code, has likely already had 10+ years of 'standard' mathematical notation drilled into them?

  Additionally, I wonder what would have happened on a societal level if prefix notation had become the 'standard' after
  it' invention/discovery. How would this have influenced mathematics/programming languages?

## Chapter Thoughts/Insights

### 1

* The `if` operator in Scheme is for 'single predicate' conditional cases (think `if_else()` in R's tidyverse).
* The `cond` operator in  Scheme is for 'multiple predicate' conditional cases (think standard `if...elif...elif...else`
  case in Python).

**Exercise 1.1**
```scheme

10
(+ 5 4 3)
(- 9 1)
(/ 6 2)
(+ (* 2 4) (- 4 6))
(define a 3)
(define b (+ a 1))
(+ a b (* a b))
(= a b)
; if ( b > a ) and (b < (a * b)), then a, otherwise b.
(if (and (> b a) (< b (* a b)))
    a
    b
)

(cond ((= a b) 6)
      ((= b 4) (+ 6 7 a))
      (else 25)
)

; ( Add 2 to ( if b > a, return b, otherwise return a ) )
(+ 2 (if (> b a) b a))

(* (cond ((> a b) a)
	 ((< a b) b)
	 (else -1))
   (+ a 1)
)
```

**Exercise 1.2**
The prefix form of the equation:
$$
\frac{5 + 4 + (2 - (3 - (6 + \frac{4}{5})))}{3(6 - 2)(2 - 7)}
$$
is:
```scheme
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5)))))
   (* 3 (- 6 2) (- 2 7))
)
```

**Exercise 1.3**

Define a procedure that takes 3 numbers as arguments and returns the sum of the squares of the larger two numbers

```scheme
(define (sum_squares_of_larger_two a b c)
  (cond
    ( (= (min a b c) c) (+ (square a) (square b)) )
    ( (= (min a b c) b) (+ (square a) (square c)) )
    ( (= (min a b c) a) (+ (square b) (square c)) )
    )
  )
```

**Newtons Method of Successive Appro

### 2

### 3

### etc

## Reasoning Checks

