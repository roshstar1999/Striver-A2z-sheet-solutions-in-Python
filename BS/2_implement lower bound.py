class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,target):
        #Your code here

        start=0
        end=len(A)-1
        maxx=-1
        while start<=end:
            mid=(start+end)//2
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                end=mid-1
            else:
                if maxx<A[mid]:
                    maxx=mid
                start=mid+1
        
        return maxx
