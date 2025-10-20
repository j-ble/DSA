class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # create a hashset to store nums
        hashset = set(nums)
        # range of numbers
        n = len(nums)
        # check every number within the range 0 + n
        for i in range(n + 1):
            # if the number is not seen in the set
            if i not in hashset:
                # return it
                return i