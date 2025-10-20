class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Optimize for time complexity - we create a hash map
        # create an empty set
        hashset = set()
        # iterate through the numbers list
        for n in nums:
            # if n is in hashset return true
            if n in hashset:
                return True
            # add elements from nums into hashset
            hashset.add(n)
        return False


        