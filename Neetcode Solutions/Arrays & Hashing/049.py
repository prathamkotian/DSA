# Group Anagrams
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        # initializing a dictionary
        temp={}
        for word in strs:
            # sorting the word
            sortedword = ''.join(sorted(word))
            
            if sortedword in temp: # appending the word for that key(sorted word)
                temp[sortedword].append(word)
            else: # adding the key along with its value to dictionary 
                temp[sortedword] = [word]
        return list(temp.values())
        
        


strs=["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

        