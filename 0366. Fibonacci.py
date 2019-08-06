class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        a = 0
        b = 1 
        while(n-1):
            b,a = a+b,b
            n -= 1
        return a
