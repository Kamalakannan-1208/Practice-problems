class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cnt=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            if max_cnt<cnt:
                    max_cnt=cnt

        return max_cnt

        