class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary = sorted(salary)[1:-1]
        return float(sum(salary)) / float(len(salary))
