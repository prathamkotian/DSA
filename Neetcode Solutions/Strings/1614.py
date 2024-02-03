# Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        # 1. Traverse the string s, set a conunter = 0 and a recorder depth = 0.
        # 2. If we meet a left parenthese (, counter += 1, if we meet a ), counter -= 1. 
        # 3. Each time we add one to the counter, we update recorder depth = max(depth, counter).

        count, depth =0, 0
        for char in s:
            if char == "(":
                count += 1
                depth = max(depth, count)
            if char == ")":
                count -= 1
        return depth


class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        mx=0

        for i in s:
            if i=='(':
                stack.append(i)
            
            if i==")":
                mx=max(mx,len(stack))
                stack.pop()
        
        return mx