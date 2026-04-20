from numpy import array, var, mean, sum, cov, random, sqrt

## Exercise 1
# A 3 variable matrix would probably be a 3x3 like this:
# [Cov(X, X) Cov(X, Y) Cov(X, Z)
#  Cov(Y, X) Cov(Y, Y) Cov(Y, Z)
#  Cov(Z, X) Cov(Z, Y) Cov(Z, Z)]

## Exercise 2
x = array([[0, 2], [1, 1], [2, 0]])

def covariance(X):
    n =len(X)
    for i in X:
        x_all = X[i][0]
        y_all = X[i][1]

    print(x_all)
covariance(x)


def x_setup(input):
    n = len(input)
    x_values = [xi for xi in input[0:n-1][0]]
    y_values = [input[xi][1] for xi in input]
        
    x_all = input[0:n-1][0]
    y_all = input[0:n-1][1]
        
    x_part = x_values - mean(x_all)
    y_part = y_values - mean(y_all)
            
    variance = sum((x_part)*(y_part))/(n - 1)
    
    print(x_all)


print(x_setup(x))
#print(cov(x))

##Exercise 3
rng = random.default_rng(seed=42)
xarr = rng.random((3, 3))
yarr = rng.random((3, 3))

#def coeff_func(x, y):
    #for value in x, y:
        #coeffs = cov(x, y)/(sqrt(cov(x)*cov(y)))
        #print(coeffs)
#coeff_func(xarr, yarr)

