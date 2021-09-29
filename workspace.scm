(RESTART 1)

(define (sum_squares_of_larger_two a b c)
  (cond
    ( (= (min a b c) c) (+ (square a) (square b)) )
    ( (= (min a b c) b) (+ (square a) (square c)) )
    ( (= (min a b c) a) (+ (square b) (square c)) )
    )
  )
