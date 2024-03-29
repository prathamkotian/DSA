# Jump Game
# Imagine you have a car, and you have some distance to travel (the length of the array). This car has some amount of gasoline, and as long as it has gasoline, it can keep traveling on this road (the array). Every time we move up one element in the array, we subtract one unit of gasoline. However, every time we find an amount of gasoline that is greater than our current amount, we "gas up" our car by replacing our current amount of gasoline with this new amount. We keep repeating this process until we either run out of gasoline (and return false), or we reach the end with just enough gasoline (or more to spare), in which case we return true.
# Note: We can let our gas tank get to zero as long as we are able to gas up at that immediate location (element in the array) that our car is currently at.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        final_idx=nums[len(nums)-1]

        for i in range(len(nums)-2,-1,-1):

            if i+nums[i]>=final_idx:
                final_idx=i
        
        return final_idx==0
            
class Solution_2:
    def canJump(self, nums: list[int]) -> bool:
        idx=0
        for i in nums:
            if idx<0:
                return False
            elif i>idx:
                idx=i
            idx-=1
        return True
            
