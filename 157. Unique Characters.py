class Solution:
    """
    @param: str: A string
    @return: a boolean
    """
    def isUnique(self, str):
        return len(str)==len(set(str))
