class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for j in jewels:
            for i in stones:
                if j ==i:
                    count+=1
        return count