package sort

func SelectionSort(arr []int) []int {
	n := len(arr)
	for step := range n {
		minIdx := step
		for i := step + 1; i < len(arr); i++ {
			if arr[i] < arr[minIdx] {
				minIdx = i
				//arr[i], arr[minIdx] = arr[minIdx], arr[i]
			}
		}
		arr[step], arr[minIdx] = arr[minIdx], arr[step]
	}
	return arr
}
