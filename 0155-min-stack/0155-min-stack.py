class MinStack(object):

    def __init__(self):
        self.s=[]
        self.st=[]

    def push(self, val):
        self.s.append(val)
        if not self.st or val<=self.st[-1]:
            self.st.append(val)

    def pop(self):
        if self.s.pop()==self.st[-1]:
            self.st.pop()
        

    def top(self):
        if not self.s:
            return -1
        else:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.st:
            return -1
        else:
            return self.st[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()