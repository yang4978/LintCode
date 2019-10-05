class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        n = len(A)
        for i in range(n,0,-1):
            for j in range(1,i):
                if(A[j-1]>A[j]):
                    A[j-1],A[j] = A[j],A[j-1]
        return A
