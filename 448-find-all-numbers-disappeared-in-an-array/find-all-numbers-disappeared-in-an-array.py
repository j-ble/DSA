class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # O(n) time complexity with O(1) space complexity
        # The problem states that every value in the array corresponds to a valid index
        # mark the existing nums (go through every value within nums)
        for n in nums:
            # Create a mapping of n to some index
            i = abs(n) - 1
            # update the nums array to negative values (shows which values exist in the array and do not exist)
            nums[i] = -1 * abs(nums[i])
        # build the result
        res = []
        # use enumerate to track the index and the number
        for i, n in enumerate(nums):
            # if the number is positive then it does not exist within the input array
            if n > 0:
                # we solved this using our index + 1. So we want to append our result to the index + 1
                res.append(i + 1)
        # return the result
        return res