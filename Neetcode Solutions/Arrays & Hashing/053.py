# Maximum Subarray

class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        
        # initializing maxi to negative infinity
        maxi=float('-inf')
        # initializing sum of nums to 0
        sum_nums=0
        for i in range(len(nums)):
            sum_nums+=nums[i]
            
            if sum_nums>maxi:
                maxi=max(sum_nums,maxi)
            
            # if sum of nums is less than 0, reset sum to 0
            if sum_nums<0:
                sum_nums=0
        if maxi:
            return maxi
        else:
            return 0
            