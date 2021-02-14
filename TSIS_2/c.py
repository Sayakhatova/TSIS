class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                if(nums[i]==nums[j+i] and i<j+i):
                    res+=1
        return res