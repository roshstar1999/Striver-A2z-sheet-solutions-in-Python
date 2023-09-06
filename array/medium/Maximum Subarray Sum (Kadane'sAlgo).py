from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n):
    maxx=arr[0]
    summ=0
    for i in arr :

        if summ+i>=0:
            summ+=i
        else:summ=0
        if maxx<summ:
            maxx=summ
    
    return maxx
