class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # create a result array to store values 
        res = []
        # m = len(matrix) & n = len(matrix[0])
        # four pointers: left and right & then a top and bottom
        # left starts of index 0 and right is going to be the length of the matrix
        # right pointer is the column, so len(matrix[0])
        left, right = 0, len(matrix[0])
        # top pointer initialized at 0 and bottom point is going to the len(matrix)
        top, bottom = 0, len(matrix)

        # need to check if the boudaries have crossed paths yet
        while left < right and top < bottom:
            # start at the lop left of the matrix and iterate through the array until we hit the right pointer
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # start iterating from the new top to the bottom pointer
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # special condition (top and bottom have met so break the while loop)
            if not (left < right and top < bottom):
                break

            # start iterating from the bottom row from right to left in reverse order
            for i in range(right -1, left -1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # start iterating from bottom to top in reverse order
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        # if boundaries cross paths return result
        return res