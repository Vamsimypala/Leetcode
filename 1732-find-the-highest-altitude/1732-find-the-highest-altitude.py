class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        v=[0]
        c=0
        for i in range(len(gain)):
            lent=c+gain[i]
            v.append(lent)
            c=lent
        return max(v)
            
            