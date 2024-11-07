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

# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the grid
# This is because we are visiting each cell in the grid only a single time

# Question 2:
# Give an algorithm to solve this problem. Determine the asymptotic time and space complexity of your algorithm
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

# Time Complexity: O(ElogV) where E is the number of edges and V is the number of vertices
# This is because we are using a heap to store the probabilities of each node and we are visiting each edge only once.
# The time complexity of the heap operations is O(logV) where V is the number of vertices. The E term comes from the
# fact that we are visiting each edge only once.
# Space Complexity: O(V) where V is the number of vertices
# This is because we are storing the probabilities of each node in the prob array which has a size of V. We are also
# using a heap to store the nodes to visit which has a maximum size of V. Thus, the space complexity is O(V).
