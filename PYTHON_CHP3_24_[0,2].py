### Paul Rizzo helped out with this code; give credit to where credit is due ###
from math import *

eps = 0.01 # Global variable
def H_eps(x, eps): # piecewise function of the smoothed Heaviside function
    if x < -eps:
        H_eps = 0
    elif -eps <= x <= eps:
        H_eps = 0.5 + (x/(2*eps)) + ((1/(2*pi))*sin((pi*x)/eps))
    elif x > eps:
        H_eps = 1
    return H_eps

    # Function code
def test_H_eps(): # function that outputs H_eps from varying given initial conditions
    print(H_eps(-1, 0.01))
    print(H_eps(-0.01, 0.01))
    print(H_eps(0, 0.01))
    print(H_eps(0.01, 0.01))
    print(H_eps(1, 0.01))
    return

    # Driver code
test_H_eps()