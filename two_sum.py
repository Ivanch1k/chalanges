class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rest = {}
        for i, n in zip(range(len(nums)), nums):
            r = rest.get(target-n, None)
            if r is not None:
                return [r, i]
            else:
                rest.update({n: i})
        return False
