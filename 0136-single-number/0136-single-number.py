class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v=set(nums)
        for i in v:
            if nums.count(i)==1:
                return i