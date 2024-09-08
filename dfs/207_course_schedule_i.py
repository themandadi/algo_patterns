#!/usr/bin/env python3

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

from typing import List, Dict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        visited: Dict[int, bool] = dict()

        for i, j in prerequisites:
            graph[i].append(j)
        
        def dfs(c):
            if c in visited:
                return visited[c]
            
            visited[c] = True

            for i in graph[c]:
                if dfs(i):
                    return True
            visited[c] = False

            return False

        for c in range(numCourses):
            if dfs(c):
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    assert solution.canFinish(2, [[1,0]])
    assert not solution.canFinish(2, [[1, 0], [0, 1]])