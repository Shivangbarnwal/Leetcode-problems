from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        mp = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1

            mp[tuple(freq)].append(s)

        return list(mp.values())
                


                        
                        