class Solution(object):
    def evalRPN(self, tokens):
        st = []

        for tok in tokens:
            if tok in ['+', '-', '*', '/']:
                b = st.pop()
                a = st.pop()

                if tok == '+':
                    st.append(a + b)
                elif tok == '-':
                    st.append(a - b)
                elif tok == '*':
                    st.append(a * b)
                else:  # '/'
                    res = abs(a) // abs(b)
                    if (a < 0) ^ (b < 0):
                        res = -res
                    st.append(res)
            else:
                st.append(int(tok))

        return st[0]

        