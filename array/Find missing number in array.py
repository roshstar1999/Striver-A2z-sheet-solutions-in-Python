def missingNumber(self, nums: List[int]) -> int:
        summ=0
        for i in nums:
            summ+=i
        n=len(nums)
        return n*(n+1)//2-summ
