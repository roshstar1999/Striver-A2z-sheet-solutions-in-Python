class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        x=0
        nums.sort()
        for j in range(len(nums)):
            k+=nums[j]
            if k <nums[j]*(j-x+1):
                k-=nums[x]
                x+=1
        return j-x+1
