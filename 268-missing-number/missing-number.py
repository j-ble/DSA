class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # space complexity O(1) & time complexity O(n)
        # find the length of the array
        n = len(nums)
        # find the range/length of nums
        for i in range(len(nums)):
            # add number and subtract actual number found
            n += (i - nums[i])
        return n