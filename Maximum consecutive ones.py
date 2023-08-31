def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx=0
        ptr=0
        countt=0
        n=len(nums)
        while ptr<n:
            if nums[ptr]==0:
                if countt>maxx:
                    maxx=countt
                countt=0
            else:
                countt+=1
            ptr+=1
        return(max(maxx,countt))
