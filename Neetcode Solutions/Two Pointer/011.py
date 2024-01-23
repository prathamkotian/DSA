# Container with most water
class Solution:
    def maxArea(self, A: [int]) -> int:
        l = 0
        r = len(A) -1
        area = 0
     
        while l < r:
        # Calculating the max area
            area = max(area, min(A[l],A[r]) * (r - l))
     
            if A[l] < A[r]:
                l += 1
            else:
                r -= 1
        return area
class Solution_2:
    def maxArea(self, height: [int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        area = 0

        while left < right:
            # if height of left is greater, then we will consider height of right*(right-left)
            # and we keep the greater value as it is and decrement right pointer
            if height[left] > height[right]:
                area = max(area, height[right] * (right - left))
                right -= 1
            # if height  of right is greater, then height of left*(right-left)
            # and we will increment left pointer    
            else:
                area = max(area, height[left] * (right - left))
                left += 1
                

        return area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
print(Solution_2().maxArea(height))