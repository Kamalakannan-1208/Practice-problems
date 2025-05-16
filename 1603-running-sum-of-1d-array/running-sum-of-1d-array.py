class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #answer
        ans=[]
        #sum
        sum= 0
        #store array logic
        for i in range(0,len(nums)):
            sum += nums[i]
            ans.append(sum)
        return ans
            
        