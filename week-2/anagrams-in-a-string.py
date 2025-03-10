# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = "".join(sorted(p))

        start_indices = []
        start_index = 0
        window = ""

        for char in s:
            window += char
            if len(window) == len(p):
                if "".join(sorted(window)) == p:
                    start_indices.append(start_index)

                start_index += 1
                window = window[1:]

        return start_indices
