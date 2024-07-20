package sort

func MergeSort(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}
	cut := len(arr) / 2
	left := MergeSort(arr[:cut])
	right := MergeSort(arr[cut:])

	arr = make([]int, len(arr))
	l, r := 0, 0
	for i := range len(arr) {
		if l >= len(left) {
			arr[i] = right[r]
			r++
		} else if r >= len(right) {
			arr[i] = left[l]
			l++
		} else {
			if left[l] < right[r] {
				arr[i] = left[l]
				l++
			} else {
				arr[i] = right[r]
				r++
			}
		}
	}
	return arr
}
