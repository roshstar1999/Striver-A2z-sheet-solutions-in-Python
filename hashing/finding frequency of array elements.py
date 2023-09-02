from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    d=[]
    for i in range(n):
        d.append(0)
    
    for i in edges:
        if i<=n:
            d[i-1]+=1

    return d

    
    
