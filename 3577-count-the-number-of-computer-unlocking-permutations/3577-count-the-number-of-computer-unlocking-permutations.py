class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        n=len(complexity)
        if complexity[0]==min(complexity) and complexity.count(min(complexity))==1:
            c=1
            while n!=1:
                n-=1
                c*=n
            return c%(10**9+7)
        return 0
        