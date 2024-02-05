# Max consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        count=0
        max_count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                max_count=max(count,max_count)
            else:
                count=0
        return max_count

print(Solution().findMaxConsecutiveOnes(nums=[0,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1]))