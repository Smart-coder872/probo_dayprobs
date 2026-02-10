from numpy import array, var, mean, sum, cov, random, sqrt

class Day4:
## Exercise 1
# A 3 variable matrix would probably be a 3x3 like this:
# [Cov(X, X) Cov(X, Y) Cov(X, Z)
#  Cov(Y, X) Cov(Y, Y) Cov(Y, Z)
#  Cov(Z, X) Cov(Z, Y) Cov(Z, Z)]

## Exercise 2
    x = array([[0, 2], [1, 1], [2, 0]])
    def x_setup(input):
        n = len(input)
        x_values = [xi[0] for xi in input]
        y_values = [xi[1] for xi in input]
        
        for xi in input:
            x_part = xi[0] - mean(x_values)
            y_part = xi[1] - mean(y_values)
            
            variance = sum((x_part)*(y_part))/(n - 1)
            print(variance)


    #print(x_setup(x))
    #print(cov(x))
##Exercise 3
rng = random.default_rng(seed=42)
xarr = rng.random((3, 3))
yarr = rng.random((3, 3))

def coeff_func(x, y):
    for value in x, y:
        coeffs = cov(x, y)/(sqrt(cov(x)*cov(y)))
        print(coeffs)
coeff_func(xarr, yarr)

