class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums = n + 1; each int in range [1, n] 
        # pigeonhole principle - at least one value must repeat once
        # without modifying the nums/input array - sorting algorithm
        # using only constant extra space - no hashset
        # pointer-based O(1) space solition - Floyd's cycle
        # nums[i] -> nums[nums[i]] ; linked list
        # initilize at fast and slow at 0
        slow, fast = 0, 0
        # infinite loop until they match
        # find where the multiple nodes point to (start of the cycle)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # when slow is equal to fast break
            if slow == fast:
                break
        # find the start of the the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
# Time Complexity: O(n) iterate thorugh the array length 
# Space Complexity: O(1) using three pointers with no extra memory 