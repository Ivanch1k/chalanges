class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        amounts = []
        for n in set(nums):
            amounts.append((n, nums.count(n)))
        return [n[0] for n in sorted(amounts, key=lambda x: x[1], reverse=True)[:k]]
