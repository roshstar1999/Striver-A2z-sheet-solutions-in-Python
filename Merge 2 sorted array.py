def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    
    al=len(a)
    bl=len(b)
    pa=0
    pb=0
    arr=[]
    while pa<al and pb<bl:
        if a[pa]==b[pb]:
            while pb<bl and a[pa]==b[pb]:
                pb+=1
            arr.append(a[pa])
            while pa<al and arr[-1]==a[pa]:
                pa+=1
            
        elif a[pa]<b[pb]:
            if not arr or arr[-1]!=a[pa]:
                arr.append(a[pa])
            pa+=1
        else:
            if not arr or arr[-1]!=b[pb]:
                arr.append(b[pb])
            pb+=1
    if pa<al:
        for i in a[pa:]:
            if arr[-1]!=i:
                arr.append(i)
    elif pb<bl:
        for i in b[pb:]:
            if arr[-1]!=i:
                arr.append(i)
    return arr



