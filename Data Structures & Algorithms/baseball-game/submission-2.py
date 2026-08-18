from collections import deque
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st=deque()
        sumi=0
        for i in range(len(ops)):
            if ops[i]=='+':
                st.append(st[-1]+st[-2])
                sumi+=st[-1]
            elif ops[i]=='C':
                sumi-=st.pop()
            elif ops[i]=='D':
                st.append(st[-1]*2)
                sumi+=st[-1]
            else:
                num=int(ops[i])
                st.append(num)
                sumi+=num
        return sumi
            
            



                