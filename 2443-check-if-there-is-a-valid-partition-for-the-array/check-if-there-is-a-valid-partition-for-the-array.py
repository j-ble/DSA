class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        # we use dynamic programming to check if array can be partitioned
        # dp[0] is True (empty array is valid)
        dp = [False] * (n + 1)
        dp[0] = True
        # dp[i] represent if nums[0:i] can be partitioned
        # we iterate through each position
        for i in range(2, n + 1):
            # we check three conditions: 2 equal, 3 equal, 3 consecutive increasing
            # conditions 1: last 2 elements are equal
            if i >= 2 and nums[i-1] == nums[i-2] and dp[i-2]:
                dp[i] = True
            # condition 2: last 3 elements are equal
            if i >= 3 and nums[i-1] == nums[i-2] == nums[i-3] and dp[i-3]:
                dp[i] = True
            # condition 3: last 3 elements are consecutivly increasing by 1
            if i >= 3 and nums[i-1] == nums[i-2] + 1 and nums[i-2] == nums[i-3] + 1 and dp[i-3]:
                dp[i] = True
        # we return if entire array can be partitioned
        return dp[n]
# Time Complexity O(n) where n is the length of nums
# Space Complexity O(n) for dp array (this could be optimized for O(1) using rolling varaibles)