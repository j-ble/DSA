class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Space Complexity is O(1) so, we must use nums array to store extra memory
        # Time Complexity is O(n) so, we iterate through the nums array
        # looking at the examples below, 0's and 1's are edge cases that we need to cover
        # first thing that we need to take care of is making sure negative values are converted to 0
        # then we can work on the second edge case of taking care of the zeros
        # our output must be from [1...len(nums) + 1]
        for i in range(len(nums)):
            # first iteration, negatives must be set to zero
            if nums[i] < 0:
                nums[i] = 0

        # second iteration, marking the numbers as seen
        for i in range(len(nums)):
            absVal = abs(nums[i])
            # must be between the vals of [1...len(nums)]
            if 1 <= absVal <= len(nums):
                if nums[absVal - 1] > 0:
                    nums[absVal - 1] *= -1
                # must set 0 to worst case scenario -(len(nums) + 1)
                elif nums[absVal - 1] == 0:
                    nums[absVal - 1] = -1 * (len(nums) + 1)

        # third iteration, finding our final value
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1