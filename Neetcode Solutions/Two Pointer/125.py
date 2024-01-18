# Valid Palindrome 
# isalnum() == True means that string is alphanumeric i.e it doesnt contain special characters
# Time Complexity O(N)
class Solution:
    def validpalindrome(self,s:str)->bool:
        # initializing left to index 0 and right to last index 
        left,right=0,len(s)-1

        while left<=right:
            # if s[left] is not alphanumeric
            if s[left].isalnum()==False:
                left+=1
            
            elif s[right].isalnum()==False:
                right-=1
                
            # left element and right element are not equal return False    
            elif s[left].lower()!=s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True
        

s="r4_ac#ec!a4r"
print(Solution().validpalindrome(s))
