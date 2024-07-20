package sort

import "cmp"

func InsertionSort[T cmp.Ordered](arr []T) []T {
	if len(arr) < 2 {
		return arr
	}
	for step := 1; step < len(arr); step++ {
		key := arr[step]
		j := step - 1
		for j >= 0 && key < arr[j] {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}

	return arr
}
