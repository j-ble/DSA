class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # create our left and right bounds
        l, r = 0, len(matrix) - 1
        # create our while loop which and make sure sequence ends when left is bigger than right
        while l < r:
            # iterate through the 2D array
            # take advantage of the i to iterate in the matrix array to shift
            for i in range(r - l):
                # top and bottom are the same as left and right boundary since n * n
                top, bottom = l, r
                # store TopLeft value in memory 
                TopLeft = matrix[top][l + i]
                # store the bottom left into the top left 
                matrix[top][l + i] = matrix[bottom - i][l]
                # store the bottom right into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # store the top right into the bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # store the TopLeft into the top right 
                matrix[top + i][r] = TopLeft
            l += 1
            r -= 1
# Time Complexity is O(n^2) since this we are iterating through n * n
# Space Complexity of O(1) since we are roating in place