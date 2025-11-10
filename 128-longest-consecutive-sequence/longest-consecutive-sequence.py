class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) Time complexity so, we must iterate through the array 
        # O(n) space complexity since we will create a hashset to store organized nums array
        # initalize our hashset and takes care of our repeatting number edge case
        hashSet = set(nums)
        # we want to return the longest consecutive element sequence
        # initalize our longest variable to 0
        longest = 0
        # iterate throught the nums array
        for n in hashSet:
            # how do we find the beginning of the sequence?
            # n - 1 is beginning of a sequence
            # also need to in
            if (n - 1) not in hashSet:
                # we need to find what our current length is of the current sequence
                # initalize our length of the sequence 
                length = 0
                # how do we know if the sequence continues?
                # does the value of our length + the n in the numbers array exist?
                while (n + length) in hashSet:
                    length += 1
                # How do we update the longest length?
                # Compare which number is higher, the length or the current longest?
                longest = max(length, longest)
        return longest


