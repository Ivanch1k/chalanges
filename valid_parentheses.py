class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for p in s:
            if p in ('(', '[', '{'):
                stack.append(p)
            else:
                search = '(' if p == ')' else '[' if p == ']' else '{'
                if stack and stack[-1] == search:
                    stack.pop()
                else:
                    return False
        
        return not stack
