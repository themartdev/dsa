package main

// To review, should use stack approach
func dailyTemperatures(temperatures []int) []int {
	offsets := make([]int, len(temperatures))

	for i := len(offsets) - 1; i >= 0; i-- {
		findWarmerOffset(temperatures, offsets, i)
	}

	return offsets
}

func findWarmerOffset(temperatures, offset []int, idx int) {
	target := temperatures[idx]
	value := 0
	i := idx + 1
	for i < len(temperatures) {
		if temperatures[i] > target {
			value = i - idx
			break
		} else if temperatures[i] == target {
			if offset[i] == 0 {
				value = 0
				break
			} else {
				value = offset[i] + (i - idx)
				break
			}
		} else {
			if offset[i] == 0 {
				value = 0
				break
			}
			i = i + offset[i]
		}
	}
	offset[idx] = value
}
