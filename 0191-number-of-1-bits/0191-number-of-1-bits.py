class Solution:
    def hammingWeight(self, n: int) -> int:
        v=bin(n)
        m=v[2:]
        f=m.count("1")
        return f
        
        