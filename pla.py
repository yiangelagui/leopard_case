#This program implements a basic version of the perceptron learning algorithm on a randomly chosen target function.
#2 dimensions. X in [-1,1]x[-1,1].
#Target function is random line in X. Inputs are random points evaluated with target function.

from random import *

#Create target function from two random points in X
pt1 = [uniform(-1,1), uniform(-1,1)]
pt2 = [uniform(-1,1), uniform(-1,1)]


if __name__ == "__main__": 
