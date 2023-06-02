class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        strs_len = len(strs)
        for i in range(0, len(strs[0])):
            if len(list(filter(lambda x: x.startswith(strs[0][:i + 1]), strs))) != strs_len:
                return prefix
            prefix += strs[0][i]
        return prefix
