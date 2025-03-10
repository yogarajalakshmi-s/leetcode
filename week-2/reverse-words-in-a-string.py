class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = ""
        print(words)
        for word in words[::-1]:
            result += word + " "

        return result.strip()
