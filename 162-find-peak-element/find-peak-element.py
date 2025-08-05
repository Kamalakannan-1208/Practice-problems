class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        s=1
        e=n-2
        while(s<=e):
            mid=(s+e)//2
            if(nums[mid-1]<nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid-1]<nums[mid]<nums[mid+1]):
                s=mid+1 
            else: 
                e=mid-1
        return -1
        