class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    
    def climbStairs(self, n):
        # if(n==0):
        #     return 0
        # factorial = [1] * (n+1)
        # for i in range(2,n+1):
        #     factorial[i] = i*factorial[i-1]
        
        # sum = 0
        # for x in range(n//2+1):
        #     y = n - 2*x
        #     sum += factorial[x+y]//factorial[x]//factorial[y]
        # return sum
        
        if(n<=2):
            return n
        a = 1
        b = 2
        for i in range(n-1):
            a,b = b,a+b
        return a
