# This is to test certain codes just to figure out how it runs

class Solution:
    def anagram(s:str,t:str):

        if len(s)!=len(t):
            return False

        dict_s={}
        dict_t={}

        for i in s:
            if i not in dict_s:
                dict_s[i]=1
            else:
                dict_s[i]+=1
        
        for i in t:
            if i not in dict_t:
                dict_t[i]=1
            else:
                dict_t[i]+=1
        
        if dict_s==dict_t:
            return True
        else:
            return False


s="anagram"
t="nagrama"
print(Solution().anagram(s,t))