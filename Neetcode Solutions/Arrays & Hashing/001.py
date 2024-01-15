def twosum(nums,target):
    n=len(nums)
    hmap={}
    for i in range(n):
        # calculate the difference of target and present element
        diff=target-nums[i]
        
        if diff in hmap:
            # returm key value of difference element i.e its index
            return [hmap[diff],i]
 
        # store current number into hash map with its index as value
        hmap[nums[i]]=i


nums=[2,7,11,15]
target=9
print(twosum(nums,target))