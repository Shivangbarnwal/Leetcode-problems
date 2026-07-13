class Solution:
    def secondsBetweenTimes(self, s: str, e: str) -> int:
        return (int(e[:2])-int(s[:2]))*3600+(int(e[3:5])-int(s[3:5]))*60+(int(e[6:])-int(s[6:]))