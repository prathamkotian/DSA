# Climbing Stairs Problem
# Solution 1 is recursive  with Time complexity O(2^N)
class Solution:
    def climbStairs(self,n):
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)
# Solution 2 is optimal with just O(N)
class Solution_2:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        array_dp=[0 for i in range(n+1)]
        array_dp[1]=1
        array_dp[2]=2

        for i in range(3,n+1):
            array_dp[i]=array_dp[i-1]+array_dp[i-2]
        return array_dp[n]
class Solution_3:
    
    def climbStairs(self, n: int) -> int:
        prev_prev=1
        prev=2
        for i in range(2, n+1):
            prev,prev_prev=prev+prev_prev,prev 
            
        return prev_prev
        

n=44
print("1.",Solution().climbStairs(n))
print("2.",Solution_2().climbStairs(n))
print("3.",Solution_3().climbStairs(n))