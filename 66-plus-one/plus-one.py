class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        no=0
        for i in digits:
            no=(no*10)+i
        no=no+1
        ans=[]
        while no>0:
            ans.insert(0,no%10)
            no=no//10
        return ans

        

        