class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix == []:
            return False
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = n*m-1
        while(start+1<end):
            mid = (start+end)//2
            if(target>matrix[mid//m][mid%m]):
                start = mid
            else:
                end = mid
        if(target==matrix[start//m][start%m]):
            return True
        if(target==matrix[end//m][end%m]):
            return True
        return False
