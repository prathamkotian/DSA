# Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums: [int]) -> [int]:
        pos_idx=0
        neg_idx=1
        res=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]>0:
                res[pos_idx]=nums[i]
                pos_idx+=2
            else:
                res[neg_idx]=nums[i]
                neg_idx+=2
        return res

class Solution_2:
    def rearrangeArray(self, nums: [int]) -> [int]:
        pos=[]
        neg=[]
        res=[]

        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            if nums[i]<0:
                neg.append(nums[i])
        i,j=0,0
        while i<len(pos) or j<len(neg):
            res.append(pos[i])
            i+=1
            res.append(neg[j])
            j+=1
        while i<len(pos):
            res.append(pos[i])
            i+=1
        while j<len(neg):
            res.append(neg[j])
            j+=1


        return res