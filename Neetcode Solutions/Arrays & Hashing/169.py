# Majority Elements

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        hmap={}

        for i in range(len(nums)):
            hmap[nums[i]]=hmap.get(nums[i],0)+1

        for i,j in hmap.items():
            if j>len(nums)//2:
                return i
