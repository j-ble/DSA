class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Space Complexity is O(n) since we create a hashSet
        # time complexity is O(n) since we iterate through array
        hashSet = set(nums)
        if len(nums) != len(hashSet):          
            return True
        return False