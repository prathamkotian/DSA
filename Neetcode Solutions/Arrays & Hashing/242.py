class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False

        count1={} # dict for s
        count2={} # dict for t
        

        # adding elements of s to dict count1
        for i in s:
            if i not in count1:
                count1[i]=1
            else:
                count1[i]+=1
        
        # adding elements of t to dict count2
        for i in t:
            if i not in count2:
                count2[i]=1
            else:
                count2[i]+=1

        if count1!=count2:
            return False

        return True
    
s="anagram"
t="nagrama"
print(Solution().isAnagram(s,t)) #True