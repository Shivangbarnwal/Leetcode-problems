class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        st=0
        for i in s:
            if st==0 and i=="(":
                st+=1
            
            elif i=="(":
                st+=1
                ans+=i
            elif i==")":
                st-=1
                if st!=0:
                    ans+=i
        return ans