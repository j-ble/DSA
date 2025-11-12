class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space Complexity O(n) since we will create a hashset
        # Time complexity is O(n) since we go through the array
        # iterate through the array and store each char in the hashset
        return Counter(s) == Counter(t)