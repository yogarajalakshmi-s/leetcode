# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        temp = 0
        stack = []

        for char in s:
            if char.isdigit():
                temp = temp * 10 + int(char)
            elif char == "[":
                stack.append(result)
                stack.append(temp)
                result = ""
                temp = 0
            elif char == "]":
                ptemp = stack.pop()
                pstring = stack.pop()
                result = pstring + ptemp * result
            else:
                result += char

        return result
