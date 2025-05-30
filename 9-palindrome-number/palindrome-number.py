class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x
        lastdigit=0
        revno=0
        while n>0:
            lastdigit= n%10
            revno=revno*10+lastdigit
            n=n//10

        return revno == x