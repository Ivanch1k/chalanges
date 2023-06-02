class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seq = ''
        max_length = 0
        for i, ch in zip(range(len(s)), s):
            if ch in seq:
                max_length = len(seq) if len(seq) > max_length else max_length
                seq = seq[seq.index(ch) + 1:]
            seq += ch
        return max(max_length, len(seq))
