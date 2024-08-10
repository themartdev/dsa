package main

// Pretty bad solution that still passes. I was missing the fact that minHeight
// can be shared between left and right heights because of the nature of the
// problem. If i,j has a min height of 0,
// we can discard any inner pillar smaller than that min height
func maxArea(height []int) int {
	// Build right order
	rightOrder := make([]int, 0)
	minVal := 0
	for i := len(height) - 1; i >= 0; i-- {
		if height[i] > minVal {
			minVal = height[i]
			rightOrder = append(rightOrder, i)
		}
	}

	maxVal := 0
	minHeight := 0
	for i := 0; i < len(height); i++ {
		if height[i] > minHeight {
			for _, j := range rightOrder {
				if j <= i {
					break
				}
				maxVal = max(maxVal, waterAmount(height, i, j))
			}
			minHeight = height[i]
		}
	}

	return maxVal
}

func waterAmount(height []int, i, j int) int {
	return (j - i) * min(height[i], height[j])
}
