class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # num_dict = {}
        # for i in A:
        #     if(i not in num_dict):
        #         num_dict[i] = 1 
        #     else:
        #         num_dict[i] = 0
        # for keys,values in num_dict.items():
        #     if(values):
        #         return keys
        num = 0
        for i in A:
            num ^= i
        return num
        
