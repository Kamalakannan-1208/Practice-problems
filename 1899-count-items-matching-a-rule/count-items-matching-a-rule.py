class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        value=0
        if ruleKey == "type":
            value=0
        elif ruleKey == "color":
            value=1
        else:
            value=2

        cnt=0
        for i in items:
            if i[value] == ruleValue:
                cnt=cnt+1
        
        return cnt
        