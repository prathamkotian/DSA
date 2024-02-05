# Missing Numbers

class Solution:
    def missingNumber(self, nums: [int]) -> int:
        n=len(nums)
        actual_sum=n*(n+1)//2
        # Sum of all elements in nums
        nums_sum=0
        for i in range(n):
            nums_sum+=nums[i]
        return actual_sum-nums_sum
    
nums=[0,1,2,3,4,6]
print(Solution().missingNumber(nums))