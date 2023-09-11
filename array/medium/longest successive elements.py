from typing import *

def longestSuccessiveElements(a : List[int]) -> int:
    # Write your code here.
    aset=set(a)
    
    
    maxx=0
    for i in aset:
        if i-1 not in aset:
            countt=0
            
            while i+countt in aset:
                
                countt+=1

            maxx=max(countt,maxx)
            
    return maxx
