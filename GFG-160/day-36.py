class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        if not mat or not mat[0]:
            return []
        
        result = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1

        while top <= bottom and left <= right:
            
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1

            
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1

            if top <= bottom:
                
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1

            if left <= right:
               
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1

        return result
