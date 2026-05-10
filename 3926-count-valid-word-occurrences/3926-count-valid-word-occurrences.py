from collections import defaultdict
class Solution(object):
    def countWordOccurrences(self, chunks, queries):
        """
        :type chunks: List[str]
        :type queries: List[str]
        :rtype: List[int]
        """

        s="".join(chunks)
        words=defaultdict(int)
        cur=""
        def is_letter(ch):
            return 'a'<=ch<='z'
        for i in range(len(s)):
            ch=s[i]
            if is_letter(ch):
                cur+=ch
            elif ch=='-' and i>0 and is_letter(s[i-1]) and i<len(s)-1 and is_letter(s[i+1]):
                cur+=ch
            else:
                if cur!="":
                    words[cur]+=1
                cur=""
        if cur!="":
            words[cur]+=1
        ans=[]
        for j in queries:
            ans.append(words[j])
        return ans