package main

func main() {
}

// m x n integer array grid
// seems like it could be solved through 2d DP,
// since the result of a m-1 x n-1 matrix directly affect the result from m x n
// let's try DP
func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	if obstacleGrid[0][0] == 1 {
		return 0
	}

	m, n := len(obstacleGrid), len(obstacleGrid[0])

	// Initialize 2d DP. DP represents the number of possible paths to reach
	// a given point
	dp := make([][]int, len(obstacleGrid))
	for i, _ := range dp {
		dp[i] = make([]int, len(obstacleGrid[0]))
	}

	// Initial condition
	dp[0][0] = 1
	for i, _ := range dp {
		for j, _ := range dp[0] {
			if i > 0 {
				dp[i][j] += dp[i-1][j]
			}
			if j > 0 {
				dp[i][j] += dp[i][j-1]
			}
			if obstacleGrid[i][j] == 1 {
				dp[i][j] = 0
			}
		}
	}
	return dp[m-1][n-1]
}

// a b c
// d e f
// g h i
