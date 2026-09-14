class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        unvisited, visiting, visited = 0, 1, 2
        states = [unvisited] * numCourses

        def dfs(node):
            if states[node] == visited:
                return True
            elif states[node] == visiting:
                return False
            states[node] = visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True