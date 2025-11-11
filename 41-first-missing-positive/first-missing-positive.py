class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        # Step 1: Cyclic Sort to place numbers in their correct spots.
        # We want to put number k at index k-1.
        while i < n:
            # The correct index for the number nums[i]
            correct_idx = nums[i] - 1

            # If the number is in the right range (1 to n)
            # AND it's not already in its correct spot...
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                # ...then swap it into its correct spot.
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                # Otherwise, move on to the next number.
                i += 1
                
        # After sorting, nums should look something like [1, 2, 3, -1, 4]
        # where the numbers are in place if possible.

        # Step 2: Find the first missing positive.
        # The first index i where nums[i] != i + 1 is our answer.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # Step 3: If all numbers from 1 to n are present...
        # ...then the missing number is n + 1.
        return n + 1