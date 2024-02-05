# Rotate array at k position
class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if k value is greater than len of arr
        if len(nums) < k:
            k = k % len(nums)

        # nums[:]=nums[-k:]+nums[:-k]

        last_k_elements = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = last_k_elements