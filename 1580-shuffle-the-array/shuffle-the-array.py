class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result=[]
        j=0
        for i in range(0,len(nums),2):
            result.insert(i,nums[j])
            result.insert(i+1,nums[j+n])
            j=j+1
        return result
            
        