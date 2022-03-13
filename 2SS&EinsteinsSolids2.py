from math import factorial
from numpy import zeros
from scipy.special import comb

from matplotlib.pyplot import bar, show

# Defining function for creating array with each macrostate

def microStateCalc(Nin):
    states = zeros(Nin)
    for i in range(Nin):
        states[i] = comb(Nin,i)

    return states

# Question 1

NGames = 5

GameMacrostates = microStateCalc(NGames)

print("Number of microstates: ", sum(GameMacrostates))

# Question 2

# You can have WWWLL, WWLWL, WLWWL,LWWWL, LWWLW, LWLWW, LLWWW, WWLLW, WLWLW, WLLWW, for a total of 10. We can check this with

print("Calculation with written function: ", GameMacrostates[3])

# Question 3

print("Check with the formula: ",factorial(NGames) / (factorial(3) * factorial(2)))

# Question 4

print("The odds are ", GameMacrostates[3] / sum(GameMacrostates) * 100, "%")

# Question 5