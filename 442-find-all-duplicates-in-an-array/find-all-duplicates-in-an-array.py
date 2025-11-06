class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # nums of length n; example1 - n = 8
        # integer of nums = 8; range = [1, 8]
        # we need a result array
        res = []
        # we need to iterate through the array once
        for n in nums:
            n = abs(n) 
            if nums[n - 1] < 0:
                res.append(n)
            nums[n - 1] = nums[n - 1] * -1
        return res

# Time Complexity: O(n) - iterate thorught the array once
# Space Complexity: O(1) - no extra memory execpt the result array