class Solution:
    """
    @param str: The identifier need to be judged.
    @return: Return if str is a legal identifier.
    """
    def isLegalIdentifier(self, str):
        if(str==""):
            return False
        for i in str:
            if("A"<=i<="Z" or "a"<=i<='z' or "0"<=i<="9" or i=="_"):
                continue
            else:
                return False
        if("0"<=str[0]<="9"):
            return False
        return True
