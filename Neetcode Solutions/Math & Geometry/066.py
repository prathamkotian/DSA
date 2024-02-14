# Plus One

class Solution:
    def plusOne(self, a: list[int]) -> list[int]:
        for i in range (len(a)-1, -1, -1):
            if a[i] == 9:
                a[i] = 0
            else:
                a[i] += 1
                return a
        return [1] + a
class Solution_2:
    def plusOne(self, digits: list[int]) -> list[int]:
        
        num=""
        for i in digits:
            num+=str(i)
        num=int(num)+1
        ans=[]
        for i in range(len(str(num))):
            ans.append(int(str(num)[i]))

        return ans
    
print(Solution().plusOne([1,2,3,9]))