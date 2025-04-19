# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_order = []
        if n <= 0:
            return sorted_order

        in_degree = {i: 0 for i in range(n)}
        graph = {i: [] for i in range(n)}

        for prerequisite in prerequisites:
            parent, child = prerequisite[1], prerequisite[0]
            graph[parent].append(child)
            in_degree[child] += 1

        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        if len(sorted_order) != n:
            return []

        return sorted_order

