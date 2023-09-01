def longestSubarrayWithSumK(a: [int], k: int) -> int:
    #solution with hashmap (optimal for boht negatives positives and zeros)
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

    #solution using sliding window
'''
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    start=0
    end=0
    n=len(a)
    maxx=0
    summ=a[0]
    while end<n and start<n:
        
        while start<=end and summ>k:
            summ-=a[start]
            start+=1

        if summ==k:
            maxx=max(maxx,end-start+1)
		
        end+=1
        if end<n:
            summ+=a[end]
            
    return maxx
'''
