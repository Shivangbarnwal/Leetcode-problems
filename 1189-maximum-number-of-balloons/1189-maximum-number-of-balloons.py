from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        mpp=Counter(text)
        return min(mpp["b"],mpp["a"],mpp["l"]//2,mpp["o"]//2,mpp["n"]) 
        