def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    hmap={}
    summ=0
    maxlen=0
    for i in range(len(a)):
        summ+=a[i]
       
        if summ==k:
           maxlen=max(maxlen,i+1)
        if summ-k in hmap.keys():
            maxlen=max(maxlen,i-hmap[summ-k])
        if summ not in hmap:
           hmap[summ]=i
        
    return maxlen
