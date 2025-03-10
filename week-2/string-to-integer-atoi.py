# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if len(s) == 0:
            return 0

        sign = -1 if s[0] == "-" else 1
        if s[0] in ["+", "-"]:
            s = s[1:]
        result = 0

        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        result *= sign
        result = min(result, 2**31 - 1)
        result = max(result, -2**31)
        return result