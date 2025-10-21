class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Create a hashset to store nums
        hashset = set(nums)
        # Create an array to store missing nums
        res = []
        # define the length of nums
        n = len(nums)
        # Find the range of nums
        for i in range(1, n + 1):
            # if i is not in the hashset, append missing num to results array
            if i not in hashset:
                res.append(i)
        # return the result
        return res