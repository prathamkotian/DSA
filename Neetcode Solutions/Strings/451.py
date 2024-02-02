# Sort Characters By Frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        hmap={}
        for i in range(len(s)):
            hmap[s[i]]=hmap.get(s[i],0)+1
        # new is type list with keys only
        new=sorted(hmap,key=hmap.get,reverse=True)
        ans=""
        for i in new:
            ans+=i*hmap[i]
        return ans

class Solution_2:
    def frequencySort(self, s: str) -> str:
        freq_dict = {}
        temp = []
        res = ""
        for i in s:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        for key, value in freq_dict.items():
            temp.append((value, key))
        
        temp = sorted(temp, reverse=True)

        for item in temp:
            res += item[1] * item[0]

        return res