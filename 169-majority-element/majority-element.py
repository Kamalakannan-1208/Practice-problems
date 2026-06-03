class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        element=-1
        for i in range(len(nums)):
            if count==0:
                element=nums[i]
                
            if element==nums[i]:
                count+=1
            else:
                count-=1
        cnt=0
        for i in nums:
            if element==i:
                cnt+=1

        if cnt>len(nums)/2:
            return element
        
        return -1
            
        
        