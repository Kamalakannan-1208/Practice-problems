class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        array=[]

        for i in range(0,len(nums)):
            array.insert(index[i],nums[i])
        
        return array


            