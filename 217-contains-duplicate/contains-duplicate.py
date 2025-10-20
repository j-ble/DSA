class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # optimize for space complexity rather than time complexity
        # sort each nums
        nums.sort()
        # iterate thoruhg sorted array
        for i in range(len(nums) - 1):
            # Compare each element with the one after it
            if nums[i] == nums[i+1]:
                # If the same return true
                return True
        # otherwise return False
        return False


        