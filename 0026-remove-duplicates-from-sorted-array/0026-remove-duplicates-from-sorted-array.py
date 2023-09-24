from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:]= dict.fromkeys(nums).keys()
        return len(nums)