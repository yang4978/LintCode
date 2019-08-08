class Solution:
    """
    @param str: the str
    @return: the sum that the letter appears the most
    """
    def mostFrequentlyAppearingLetters(self, str):
        letter_dict = {}
        for i in str:
            if i not in letter_dict:
                letter_dict[i] = 1 
            else:
                letter_dict[i] += 1
        return max(letter_dict.values())
