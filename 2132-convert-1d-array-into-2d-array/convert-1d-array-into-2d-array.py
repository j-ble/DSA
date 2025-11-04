class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # edge case: if n * m != orginal return the array
        if len(original) != n * m:
            return []
        # create an empty result array to store result
        res = []
        # each row is created by the range(m)
        for r in range(m):
            # start index (which is the row * n)
            start = r * n
            # end index (which is the start + n)
            end = start + n
            res.append(original[start:end])
        return res
# Time Complexity is O(n * m) because the loop runs m times and the cost of creating the slice is O(n)
# Space Complexity is O(n * m) because the space need grows with the size of the input array