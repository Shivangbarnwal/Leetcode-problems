class Solution:
    def minInsertions(self, s: str) -> int:
        new=""
        ins=0
        n=len(s)
        i=0
        while i < n:
            if s[i]=="(":
                new+=s[i]
            elif s[i]==")" and (i+1)<n and s[i+1]==")":
                i+=1
                new+=")"
            elif s[i]==")":
                ins+=1
                new+=")"
            i+=1
        st=0
        for i in new:
            if i=="(":
                st+=1
            else:
                st-=1
            if st==-1:
                ins+=1
                st=0
        ins+=(2*st)
        return ins