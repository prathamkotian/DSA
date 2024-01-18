# Product of array expect self
# Time Complexity O(2N)
# Space Complexity O(N)
class Solution:
    def product(self,arr):
        # creating result list with 1's initialized
        res=[1]*len(arr) 
        # Calculating prefix product and storing in res
        prefix=1
        for i in range(len(arr)):
            res[i]=prefix
            prefix=prefix*arr[i]
        # Calculating postfix product and multiplying to res
        postfix=1
        for i in range(len(arr)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*arr[i]

        return res
# Solution 2 is using Time Complexity O(3N) & Space Complexity O(3N)
class Solution_2:
    def product(self,arr):
        prefix=[1]*len(arr)
        postfix=[1]*len(arr)
        ans=[]
        # Creating Prefix Array
        for i in range(1,len(arr)):
            prefix[i]=prefix[i-1]*arr[i-1]
        # Creating Postfix Array
        for i in range(len(arr)-2,-1,-1):
            postfix[i]=postfix[i+1]*arr[i+1]
        # Multiplying both
        for i in range(len(arr)):
            ans.append(prefix[i]*postfix[i])
        
        return ans



nums=[1,2,3,4]
print(Solution().product(nums))
print(Solution_2().product(nums))