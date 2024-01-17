# Two Sum
# line 8 its i+1 because the index starts from 1 not 0
def twoSum(nums,target):
    hmap={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in hmap:
            return ([hmap[diff],i+1])
        else:
            hmap[nums[i]]=i+1

nums=[2,7,11,15]
target = 9
print(twoSum(nums,target))

#-----------------------------------------------------
# given input array is sorted and it can also be solved with two pointer approach
def twoSum(nums,target):
    left,right=0,len(nums)-1
    while left <=right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return [left+1,right+1]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return [-1,-1]