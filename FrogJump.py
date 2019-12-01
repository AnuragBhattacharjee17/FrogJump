# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    p=Y-X
    return(math.ceil(p/D))