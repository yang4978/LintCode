class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        char_dict = {}
        for i in str:
            if(i not in char_dict):
                char_dict[i] = 1
            else:
                char_dict[i] += 1
        for key,value in char_dict.items():
            if(value==1):
                return key
