# Question 1:
# Give an algorithm to solve this problem and determine the asymptotic time complexity depending on the size m x n
# of the grid.
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"  # Mark the cell as visited
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1
        return count

# Question 2:
# Give an algorithm to solve this problem. Determine the asymtotic time and space complexity of your algorithm
# depending on the number of vertices V of the graph and the number of edges E of the graph. (Hint: logarithms convert
# multiplication to addition)
# https://leetcode.com/problems/path-with-maximum-probability/description/

class Solution2:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        prob = [0] * n
        prob[start_node] = 1
        pq = [(-1, start_node)]
        while pq:
            p, node = heapq.heappop(pq)
            if node == end_node:
                return -p
            for nei, p2 in graph[node]:
                if -p * p2 > prob[nei]:
                    prob[nei] = -p * p2
                    heapq.heappush(pq, (p * p2, nei))
        return 0

