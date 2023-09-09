def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    n=len(a)
    maxx=-1
    res=[]
    for i in range(n-1,-1,-1):
        if a[i]>maxx:
            maxx=a[i]
            res.append(a[i])
    return res
