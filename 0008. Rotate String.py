class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        offset = len(s)-offset%max(1,len(s))
        s[:offset] = s[:offset][::-1]
        s[offset:] = s[offset:][::-1]
        s[:] = s[:][::-1]
