class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr=range(len(nums))
        for i in range(len(nums)):
            arr[i]=nums[nums[i]]
        return arr