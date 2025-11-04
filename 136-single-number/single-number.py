class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # twice except for one. XOR "^" function
        # set our result = 0
        res = 0
        for n in nums:
            res = n ^ res
        return res
# Time Complexity O(n) since it iterates through every number in the array
# Space Complexity O(1) since there is no extra data structure is create and only on variable is used. 
