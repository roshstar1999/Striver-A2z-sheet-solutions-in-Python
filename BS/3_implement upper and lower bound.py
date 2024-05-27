
def getFloorAndCeil(arr, n, x):
    
    
    start=0
    end=n-1
    arr.sort()
    ubound=float("inf")
    lbound=-float("inf")
    while start<=end:
    
        mid=(start+end)//2
        if arr[mid]==x:
            return [str(arr[mid]),str(arr[mid])]
        
        
        if arr[mid]>x:
            if ubound>arr[mid]:
                ubound=arr[mid]
                
                
            end=mid-1
        else:
            if lbound<arr[mid]:
                lbound=arr[mid]
            
            start=mid+1
    if ubound==float("inf"):
        ubound=-1
    return [str(max(-1,lbound)),str(ubound)]
