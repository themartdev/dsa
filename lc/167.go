package main

func twoSum(numbers []int, target int) []int {
	low, high := 0, len(numbers)-1

	for high > low {
		total := numbers[low] + numbers[high]

		if total == target {
			return []int{low + 1, high + 1}

		} else if total > target {
			high--
		} else {
			low++
		}
	}

	panic("No solution found")
}
