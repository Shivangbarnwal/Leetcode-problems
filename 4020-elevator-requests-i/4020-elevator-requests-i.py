class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        i=0
        c=0
        for j in requests:
            c+=abs(i-j)
            i=j
        return c