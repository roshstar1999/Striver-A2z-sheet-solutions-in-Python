from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    d={}
    for i in v:
        if i not in d:
            d[i]=0
        d[i]+=1
    minn=[0,float('inf')]
    for i in d.keys():
        if d[i]==minn[1]:
            if minn[0]>i:
                minn[0]=i
        if d[i]<minn[1]:
            minn=[i,d[i]]
    maxx=[0,-1]
    for i in d.keys():
        if d[i]==maxx[1]:
            if maxx[0]>i:
                maxx[0]=i
        if d[i]>maxx[1]:
            maxx=[i,d[i]]
    return(maxx[0],minn[0])


    
