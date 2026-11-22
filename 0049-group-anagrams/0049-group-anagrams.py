class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans={}
        for i in strs:
            temp="".join(map(str,sorted(i)))
            if temp in ans.keys():
                ans[temp].append(i)
            else:
                ans[temp]=[i]
        return list(ans.values())