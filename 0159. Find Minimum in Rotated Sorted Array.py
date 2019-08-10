class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # temp = [nums[0],nums[-1]]
        # for i in range(1,len(nums)-1):
        #     if(nums[i]<nums[i-1] and nums[i]<nums[i+1]):
        #         temp.append(nums[i])
        #         break
        # return min(temp)
        start = 0
        end = len(nums)-1
        while(start+1<end):
            mid = (start+end)//2
            if(nums[mid]>nums[end]):
                start = mid
            else:
                end = mid
        return min(nums[start],nums[end])
