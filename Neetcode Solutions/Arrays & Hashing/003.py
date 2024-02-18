# Longest Substring Without Repeating Characters
# using hashset and sliding window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        char_set=set()
        res=0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            res=max(res,r-l+1)

        return res

        