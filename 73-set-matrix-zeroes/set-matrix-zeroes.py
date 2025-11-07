class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # "must do it in place" so with Space Complexity O(1) 
        # calculate the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        # based on diagram, special memory variable set to 0 aka False (Update to True is needed)
        rowZero = False

        # determine what rows and columns need to be set to zero
        # so we need iterate through every row and every column
        for r in range(ROWS):
            for c in range(COLS):
                # in the matrix if we find a value equal to zero
                if matrix[r][c] == 0:
                    # we need to store 0 in the row at that value
                    matrix[0][c] = 0
                    # if the row is greater than 0 
                    if r > 0:
                        # then set the column to 0 in the row (we cannot do this for the top left position)
                        matrix[r][0] = 0
                    # otherwise
                    else:
                        # we need to update our boolean/top left position to True
                        rowZero = True
                        
        # iterate thorugh the rows and columns but this time we need to skip the first row and first column
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if the row is zero or if column is zero, we want to set current position in the matrix to 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # check if origin of matrix is zero, if so, set every value in column of matrix to zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # if rowZero is true we go through every value in the first row, then we zero out the row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0