# Check if Array Is Sorted and Rotated

class Solution:
    def check(self, nums: [int]) -> bool:
        count=0
        # counting the pairs that are not in sorted order
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
        # comparing last element with first
        if nums[0]<nums[-1]:
            count+=1
        return count<=1

nums=[5,6,1,2,3,4]
print(Solution().check(nums))