class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        if 'a' in s[s.index('b'):]:
            return False
        return True