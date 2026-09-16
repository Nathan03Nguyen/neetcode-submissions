class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_cost = 0
        visited = set()
        min_heap = [(0, 0)]

        while len(visited) < len(points):
            dist, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += dist
            xi, yi = points[i]
            
            for j in range(len(points)):
                if j not in visited:
                    xj, yj = points[j]
                    nei_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_dist, j))
        return total_cost