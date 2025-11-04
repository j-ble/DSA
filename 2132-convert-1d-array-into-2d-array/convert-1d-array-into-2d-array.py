class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # 0-indexed 1-dimensional (1D) integer array original
        # e.g., [1,2,3,4]
        # two integers, m and n
        # using all the elements from original
        # if the length of original is odd return array (e.g., example 2)
        if len(original) != n * m:
            return []
        # create a result array to store new 2D Array
        res = []
        # conduct the new 2D array
        # new range for the 2D array (why? tells which slice of the original array to grab)
        # we need to loop m times becuase we need m rows
        for r in range(m):
            # get our starting index (current row * n)
            start = r * n
            # get our ending index
            end = start + n
            # slice the original 
            res.append(original[start:end])
        return res