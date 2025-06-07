class Solution(object):
    

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def last( nums, target, low, high):
            last=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    last=mid
                    low=mid+1
            return last

        def first( nums, target, low, high):
            first=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    first=mid
                    high=mid-1
            return first
            
        low=0
        high=len(nums)-1
        value1=first(nums, target, low, high)
        value2=last(nums, target, low, high)
        return [value1, value2]
        
        