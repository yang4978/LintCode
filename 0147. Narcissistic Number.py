class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        result = []
        if(n==1):
            result = [0]
        for i in  range(10**(n-1),10**n):
            sum = 0
            num = i
            while(num):
                sum += (num%10)**n
                num //= 10
            if(sum==i):
                result.append(i)
        return result
