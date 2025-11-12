class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the array 
        left, right = 0, 1 
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
# Time complexity O(n^2) using two nested loops
# Space complexity O(1) since we are iterating in place
