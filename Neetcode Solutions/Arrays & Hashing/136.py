# Single Number
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        hmap={}
        n=len(nums)

        for i in range(n):
            hmap[nums[i]]=hmap.get(nums[i],0)+1
        
        for i,j in hmap.items():
            if j==1:
                return i