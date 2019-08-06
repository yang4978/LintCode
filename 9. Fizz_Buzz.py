class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        result = ['x']*n
        for i in range(1,n+1):
            if(i%5!=0 and i%3!=0):
                result[i-1] = str(i)
            else:
                result[i-1] = (i%3==0)*"fizz"+(i%3==0)*(i%5==0)*" "+(i%5==0)*"buzz"
        return result
