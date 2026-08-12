class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def check(s):
            q=''.join(c for c,f in Counter(s).items() if f<k)
            if q:
                return max(check(t) for t in split(f'[{q}]', s))
            else:
                return len(s)
        return check(s)