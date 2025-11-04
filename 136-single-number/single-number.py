class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # twice except for one. XOR "^" function
        # set our result = 0
        res = 0
        for n in nums:
            res = n ^ res
        return res
