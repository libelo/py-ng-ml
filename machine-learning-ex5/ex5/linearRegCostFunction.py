from numpy import *

def linearRegCostFunction(X, y, theta, lambda_):
    #LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear
    #regression with multiple variables
    #   J, grad = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the
    #   cost of using theta as the parameter for linear regression to fit the
    #   data points in X and y. Returns the cost in J and the gradient in grad

    # Initialize some useful values
    m = len(y) # number of training examples

    # You need to return the following variables correctly
    J = 0
    grad = zeros(shape(theta))

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost and gradient of regularized linear
    #               regression for a particular choice of theta.
    #
    #               You should set J to the cost and grad to the gradient.
    #

    J = sum((dot(X,theta) - y)**2)/(2*m) + lambda_/(2*m)*sum(theta[1:]**2)
    grad = 1/m*dot(X.T,(dot(X, theta)-y)) + lambda_/m*hstack([array([0]), theta[1:]])
    

    # =========================================================================

    return J, grad
