from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        
        max_moves = 0  # Track the overall maximum moves

        # Fill DP table from right to left (starting from second last column)
        for j in range(n - 2, -1, -1):
            for i in range(m):
                # Check the three possible directions in the next column
                for ni in (i - 1, i, i + 1):
                    if 0 <= ni < m and grid[ni][j + 1] > grid[i][j]:
                        dp[i][j] = max(dp[i][j], dp[ni][j + 1] + 1)
                
                # Update the overall maximum moves
                if j == 0:  # Only update for the first column
                    max_moves = max(max_moves, dp[i][j])

        return max_moves
