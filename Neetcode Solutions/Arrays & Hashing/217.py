# Time Complexity O(N)
# Space Complexity O(N)

class Solution:
    def containsDuplicate(self, arr: [int]) -> bool:
        
        # declaring Hashmap
        hmap={}

        for i in arr:
            # if element is already in hmap 
            if i in hmap:
                return True
            
            # add that count of that element
            hmap[i]=hmap.get(i,0)+1
            
        return False
    
arr=[1,2,3,5,9]
print(Solution().containsDuplicate(arr)) 

#------------------------------------------------------------

# Set doesnt store dublicate elements  

class Solution:
   def containsDuplicate(self, nums: [int]) -> bool:
       if len(nums) == len(set(nums)):
           return False
       # which means len(nums) >len(set(nums)) => Dublicate elements present
       return True 