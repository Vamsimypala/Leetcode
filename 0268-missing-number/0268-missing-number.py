class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=-1
        for i in range(len(nums)):
            if i not in nums:
                c=i
        if c==-1:
            return len(nums)
        else:
            return c
            