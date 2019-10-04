class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        result = 0
        m = len(matrix)
        n = len(matrix[0])
        if(n==0):
            return 0
        i,j = m-1,0
        while(i>=0 and j<n):
            if(matrix[i][j]==target):
                result += 1
                i -= 1
                j += 1
            elif(matrix[i][j]<target):
                j += 1
            else:
                i -= 1
            
        return result
