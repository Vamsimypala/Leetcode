class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v=list(set(nums))
        v.sort()
        if len(v)>2 :
            for i in range(2):
                v.pop()
            return v[-1]
        else:
            return max(v)
            
             
            
        