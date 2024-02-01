# Longest Common Prefix
# we Shall sort the list and compare only the first and last element
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]

        for i in range(len(min(first,last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans