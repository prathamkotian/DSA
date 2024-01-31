# Remove Outermost Parentheses
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ""
        for char in s:
            if char == "(":
                if count > 0:
                    result += char
                count += 1
            else:
                count -= 1
                if count > 0:
                    result += char
        return result
    
class Solution_2:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0

        for i in s:
            if i=="(" and count==0:
                count+=1
            elif i=="(" and count>=1:
                res+=i
                count+=1
            elif i==")" and count>1:
                res+=i
                count-=1
            elif i==")" and count==1:
                count-=1
        return res