class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        while(b):
            a,b = a^b&0x7FFFFFFF, (a & b)<<1  
            #when a number is larger than 0x7FFFFFFF, type will be automatically converted from int to long
            #so its meaningful to and with 0x7FFFFFFF
        return a
