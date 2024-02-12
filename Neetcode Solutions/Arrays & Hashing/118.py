# Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        def ncr(n):
            rlist=[]
            rlist.append(1)
            res=1
            for i in range(1,n):
                res=res*(n-i)
                res/=i
                rlist.append(int(res))
            return rlist


        res=[]
        for i in range(1,numRows+1):
            res.append(ncr(i))
        return res