class Solution(object):
    def reverse(self, given_no):
        """
        :type x: int
        :rtype: int
        """
        rev_no=0

        if given_no <0:
            sign=-1
            given_no=given_no*sign
            print(given_no)
        else:
            sign=1


        while given_no:
            last_digit= given_no%10
            print("last digit",last_digit)
            rev_no= rev_no*10+last_digit
            given_no=given_no//10


        if (rev_no >= 2 ** 31 - 1) or (rev_no <= -(2 ** 31)):
            rev_no=0

        return sign*rev_no
        