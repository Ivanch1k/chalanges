class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0) != 0:
            return 0
        if len(filter(lambda x: x < 0, nums)) % 2 != 0:
            return -1
        return 1

      
# second solution with beter memory and runtime performance
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negative_amount = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negative_amount += 1
        return 1 if negative_amount % 2 == 0 else -1
