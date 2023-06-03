class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_int = -2147483648
        max_int = 2147483647

        sign = -1 if x < 0 else 1

        x = int(str(x)[1:][::-1]) if sign == -1 else int(str(x)[::-1])

        if x > max_int or x < min_int:
            return 0
        else:
            return x * sign
