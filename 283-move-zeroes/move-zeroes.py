class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Quicksort Algo
        # Left pointer starting a the index 0
        l = 0
        # right pointer that will go through the nums array
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                # update left point 
                l += 1
        # return the number
        return nums
# Time complexity O(n) since it iterates through the array once
# Space complexity O(1) since the operation is done in place without extra memory