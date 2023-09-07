def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    pos=0
    neg=0
    n=len(a)
    ans=[]
    while pos<n and neg<n:
        while pos<n and a[pos]<0:
            pos+=1
        ans.append(a[pos])
        pos+=1
        while neg<n and a[neg]>=0:
            neg+=1
        
        ans.append(a[neg])
        neg+=1
    for i in range(n):
        a[i]=ans[i]
    return a
