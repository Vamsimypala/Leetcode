class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=1
        for i in range(k):
            b=nums[-1]
            nums.pop()
            nums.insert(0,b)
        return nums
            
        