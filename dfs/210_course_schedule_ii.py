#!/usr/bin/env python3

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from typing import List, Dict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph: List = [[] for _ in range(numCourses)]
        result: List = []
        for i,j in prerequisites:
            graph[i].append(j)
        
        visited: Dict[int, List[int]] = dict()
        def dfs(i):
            if i in visited:
                return visited[i]
            
            visited[i] = True

            for j in graph[i]:
                if dfs(j):
                    return True
            
            visited[i] = False
            result.append(i)

        for i in range(numCourses):
            if dfs(i):
                return []

        return result


if __name__ == "__main__":
    solution = Solution()

    print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))