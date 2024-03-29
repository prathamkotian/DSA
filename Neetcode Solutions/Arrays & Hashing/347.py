# Top K frequent elements
# Time Complexity O(N+NlogN) beacuse of sorting
# Space complecity O(N) 
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        num_store = {}
        # adding element count to dictionary
        for num in nums:
            if num in num_store:
                num_store[num] += 1
            else:
                num_store[num] = 1

        # this sorts the key based on the values and returns in type LIST
        # sorted_nums is LIST
        sorted_nums = sorted(num_store, key=num_store.get, reverse=True)
        print(num_store)
        # returns first k key values 
        return sorted_nums[:k]

nums = [1,2]
k = 2
print(Solution().topKFrequent(nums,k))
 