
class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        summ=n*(n+1)//2
        summsquares=n*(n+1)*(2*n+1)//6
        
        s=sum(arr)
        sq=sum(a*a for a in arr)
        
        #x-y
        r_m=s-summ
        eq1=r_m
        #sqx^2-y^2
        rq_mq=sq-summsquares
        
        #x+y
        eq2=rq_mq//r_m
        
        x=(eq1+eq2)//2
        y=(eq2-eq1)//2
        return(x,y)
