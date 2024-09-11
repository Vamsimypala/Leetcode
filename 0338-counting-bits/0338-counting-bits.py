class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[]
        v=[]
        m=0
        for i in range(n+1):
            b.append(i)
        for i in b:
            c=bin(i)
            m=c[2:]
            n=m.count("1")
            v.append(n)
        return v
            
            
        