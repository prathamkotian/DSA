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
        res = 0

        while left < right:
            if height[left] > height[right]:
                res = max(res, height[right] * (right - left))
                right -= 1

            else:
                res = max(res, height[left] * (right - left))
                left += 1
                

        return res

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
print(Solution_2().maxArea(height))