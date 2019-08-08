class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        if length==0:
            return length
            
        result = length + 2*string.count(" ")
        x = result - 1
        for l in range(length-1,-1,-1):
            if(string[l]==' '):
                string[x] = '0'
                string[x-1] = '2'
                string[x-2] = '%'
                x -= 3
            else:
                string[x] = string[l]
                x -= 1
            
        return result
