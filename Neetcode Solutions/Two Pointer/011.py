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

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))