class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # result = 0
        # flag = 0
        # if(num<0):
        #     num = -num-1
        #     flag = 1
        # while(num):
        #     result += num%2
        #     num //= 2
        # return 32-result if flag else result
        total = 0
        for i in range(32):
            total += num & 1
            num >>= 1
        return total
