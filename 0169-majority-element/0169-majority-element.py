class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)/2
        num=set(nums)
        for i in num:
            v=nums.count(i)
            if v>n:
                return i
        