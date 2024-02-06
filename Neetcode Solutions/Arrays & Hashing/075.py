# Sort colours

class Solution:
    def sortColors(self, nums: [int]) -> None:

        low=0
        mid=0
        high=len(nums)-1

        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[high],nums[mid]=nums[mid],nums[high]
                high-=1


class Solution_2:
    def sortColors(self, nums: [int]) -> None:
    
        count_0=0
        count_1=0
        count_2=0

        for i in nums:
            if i==0:
                count_0+=1
            if i==1:
                count_1+=1
            if i==2:
                count_2+=1
        
        for i in range(count_0):
            nums[i]=0
        for i in range(count_0,count_0+count_1):
            nums[i]=1
        for i in range(count_0+count_1,len(nums)):
            nums[i]=2