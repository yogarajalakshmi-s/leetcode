# https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/

from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        queue = deque([1] + [0] * (forget - 1))
        count = 0
        pre = delay - 1

        for _ in range(1, n):
            count += queue[pre] - queue.pop()
            queue.appendleft(count % (10 ** 9 + 7))

        return sum(queue) % (10 ** 9 + 7)
