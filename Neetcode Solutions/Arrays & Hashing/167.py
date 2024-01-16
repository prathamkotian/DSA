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