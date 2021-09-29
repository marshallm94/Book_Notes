def good_enough(guess, x, threshold=0.01):
    if abs(x - guess) > threshold:
        return False
    elif abs(x - guess) <= threshold:
        return True

def improve_guess(old_guess, x):
    quotient = x/old_guess
    new_guess = ( old_guess + quotient ) / x
    return new_guess

def sqrt_iter(x, guess):
    if good_enough(x, guess):
        return guess
    elif not good_enough(x, guess):
        new_guess = improve_guess(old_guess=guess, x=x)
        print(new_guess)
        sqrt_iter(x=x, guess=new_guess)

print(sqrt_iter(9, 3))
