# https://leetcode.com/problems/word-break/description/

class Trie(object):

    def __init__(self):
        self.root = {'*': '*'}

    def insert(self, word):
        current = self.root

        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current['*'] = '*'

    def search_word(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]

        if '*' in current:
            return True
        else:
            return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for w in wordDict:
            trie.insert(w)

        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and trie.search_word(s[j:i]):
                    dp[i] = True
                    break

        return dp[-1]
