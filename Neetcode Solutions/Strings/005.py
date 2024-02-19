# Longest Palindrome substring

class Solution:
    def longestPalindrome(self, s: str) -> str:

        len1 = len(s)
        if len1 <= 1:
            return s

        def ret_palstr(l,r):
            while l >= 0 and r < len1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        max_str = s[0]

        for i in range(len1-1):
            o = ret_palstr(i,i)
            e = ret_palstr(i,i+1)

            if len(o) > len(max_str):
                max_str = o
            if len(e) > len(max_str):
                max_str = e

        return max_str


class Solution_2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
        
        
        