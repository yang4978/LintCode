class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        num_dict = {}
        for i in range(len(numbers)):
            num_dict[numbers[i]] = i
        for i in range(len(numbers)):
            if((target-numbers[i]) in num_dict):
                return [i,num_dict[target-numbers[i]]]
