def getFloorAndCeil(a, n, x):
   
    # Write your code here.
    
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if a[mid]==x:
            return (a[mid],a[mid])
        elif a[mid]>x:
            end=mid-1
        else:
            start=mid+1
    
    
        

        
    if mid-1>=0 :
        if mid+1<=n-1:
            if a[mid]<x:
                return (a[mid],a[mid+1])
            else:
                return (a[mid-1],a[mid])

        else:
            return (a[mid],-1)
    else:
        return (-1,a[mid])


    # Write your code here.
