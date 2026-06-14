class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_set=set(nums)
        longest_len=0
        for i in arr_set:
            if i-1 not in arr_set:
                cnt=1
                while i+1 in arr_set:
                    cnt=cnt+1
                    i=i+1
                longest_len=max(longest_len,cnt)
        return longest_len
        


