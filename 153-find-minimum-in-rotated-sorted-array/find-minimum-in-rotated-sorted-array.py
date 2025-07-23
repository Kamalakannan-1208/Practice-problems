import sys
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        e=len(nums)-1
        ans= nums[0]
        while(s<=e): 
            mid=(s+e)//2
            if nums[s]<=nums[mid]:
                ans=min(ans,nums[s])
                s=mid+1
            else:
                ans=min(ans,nums[mid])
                e=mid-1
        return ans

        