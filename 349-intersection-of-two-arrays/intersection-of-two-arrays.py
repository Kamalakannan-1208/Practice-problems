class Solution(object):
    def intersection(self, num1, num2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        ans=[]
        if len(num1)>=len(num2):
            for i in range(len(num2)):
                if num2[i] in num1:
                    ans.append(num2[i])
        if len(num2)>=len(num1):
            for i in range(len(num1)):
                if num1[i] in num2:
                    ans.append(num1[i])
        return list(set(ans)) 

        