class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if(len(source)==0 and len(target)==0):
            return 0
        result = -1
        for i in range(len(source)):
            if(source[i:i+len(target)]==target):
                return i
        return result
