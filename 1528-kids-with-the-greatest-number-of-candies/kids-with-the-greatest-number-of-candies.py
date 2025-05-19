class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        boolarr=[]
        greatest=-1
        for cady_ in candies:
            if cady_> greatest:
                greatest =cady_
        for candy in candies:
            if greatest > candy + extraCandies:
                boolarr.append(False)
            else:
                boolarr.append(True)
        return boolarr